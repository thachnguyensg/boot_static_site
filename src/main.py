from htmlnode import HTMLNode
from textnode import (
    TextNode,
    text_node_to_html_node,
    text_type_text,
    text_type_bold,
)
from inline_markdown import split_nodes_delimiter


def main():
    tnode = TextNode("This is a test node", "bold", "https://www.boot.dev")
    print(tnode)

    node = HTMLNode(
        "a", "hehe", "", {"href": "https://www.google.com", "target": "_blank"}
    )
    print(node.props_to_html())
    print(node)

    tnode = TextNode("This is a test node", "bold", "https://www.boot.dev")
    print(tnode)
    print(text_node_to_html_node(tnode))

    tnode = TextNode("This is a test node", "link", "https://www.boot.dev")
    print(text_node_to_html_node(tnode))

    test_split_nodes_delimiter()


def test_split_nodes_delimiter():
    print("Test split nodes delimiter")
    # node = TextNode("This is text with a `code block` word", text_type_text)
    # new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    # print(node)
    # print(new_nodes)
    #
    # node = TextNode("This is text with a `code block`", text_type_text)
    # new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    # print(node)
    # print(new_nodes)
    #
    node = TextNode(
        "This is text with a **bolded word** and **another**", text_type_text
    )
    new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
    print(node)
    print(new_nodes)


main()
