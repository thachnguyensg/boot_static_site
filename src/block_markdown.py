import re

from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import text_to_textnode
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    blocks = []
    if len(lines) == 0:
        return blocks

    block = []
    prev = lines[0]
    for line in lines:
        if prev == line == "":
            continue

        if line == "" and len(block) > 0:
            blocks.append("\n".join(block))
            block = []
        else:
            block.append(line.strip())
        prev = line

    if len(block) > 0:
        blocks.append("\n".join(block))

    return blocks


def block_to_block_type(block):
    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    if block.startswith("> "):
        for line in block.split("\n"):
            if not line.startswith("> "):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* ") or block.startswith("- "):
        for line in block.split("\n"):
            if not block.startswith("* ") and not block.startswith("- "):
                return block_type_paragraph
        return block_type_ulist
    if re.match(r"^\d+\. ", block):
        lines = block.split("\n")
        for i in range(len(lines)):
            if not lines[i].startswith(f"{i+1}. "):
                return block_type_paragraph
        return block_type_olist

    return block_type_paragraph


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children = []
    for block in blocks:
        if block_to_block_type(block) == block_type_heading:
            children.append(_heading_to_html(block))
        elif block_to_block_type(block) == block_type_paragraph:
            children.append(_paragraph_to_html(block))
        elif block_to_block_type(block) == block_type_quote:
            children.append(_quote_to_html(block))
        elif block_to_block_type(block) == block_type_ulist:
            children.append(_list_to_html(block, block_type_ulist))
        elif block_to_block_type(block) == block_type_olist:
            children.append(_list_to_html(block, block_type_olist))
        elif block_to_block_type(block) == block_type_code:
            children.append(_code_to_html(block))
        else:
            raise ValueError("Invalid block type")

    container = ParentNode("div", children)
    return container


def _heading_to_html(heading):
    if heading.startswith("# "):
        return LeafNode("h1", heading[2:])
    if heading.startswith("## "):
        return LeafNode("h2", heading[3:])
    if heading.startswith("### "):
        return LeafNode("h3", heading[4:])
    if heading.startswith("#### "):
        return LeafNode("h4", heading[5:])
    if heading.startswith("##### "):
        return LeafNode("h5", heading[6:])
    if heading.startswith("###### "):
        return LeafNode("h6", heading[7:])


def _paragraph_to_html(block):
    text = " ".join(block.split("\n"))
    children = []
    nodes = text_to_textnode(text)
    for node in nodes:
        children.append(text_node_to_html_node(node))

    p = ParentNode("p", children)
    return p


def _quote_to_html(quote):
    text = " ".join(map(lambda q: q[2:], quote.split("\n")))
    children = []
    nodes = text_to_textnode(text)
    for node in nodes:
        children.append(text_node_to_html_node(node))

    quote = ParentNode("blockquote", children)
    return quote


def _code_to_html(code):
    text = " ".join(code.split("\n"))
    children = []
    nodes = text_to_textnode(text)
    for node in nodes:
        children.append(text_node_to_html_node(node))

    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def _list_to_html(list, type):
    lists = list.split("\n")
    children = []
    for text in lists:
        childs = []
        nodes = text_to_textnode(text[2:].strip())
        for node in nodes:
            childs.append(text_node_to_html_node(node))

        linode = ParentNode("li", childs)
        children.append(linode)

    list_type = ""
    if type == block_type_ulist:
        list_type = "ul"
    else:
        list_type = "ol"

    list = ParentNode(list_type, children)
    return list
