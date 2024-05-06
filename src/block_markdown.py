import re

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
