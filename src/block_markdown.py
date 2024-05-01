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
