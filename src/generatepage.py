import os

from block_markdown import markdown_to_html_node, markdown_to_blocks


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    if not os.path.exists(from_path):
        raise ValueError(f"{from_path} not exist")
    if not os.path.exists(template_path):
        raise ValueError(f"{template_path} not exist")

    print("Reading content...")
    markdown = ""
    with open(from_path, "r", encoding="utf-8") as file:
        markdown = file.read()

    html = markdown_to_html_node(markdown)
    content = html.to_html()
    title = extract_title(markdown)

    print("Preparing template")
    template = ""
    with open(template_path, "r", encoding="utf-8") as file:
        template = file.read()

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", content)

    print("Writing to destination")
    dir_dest_path = os.path.dirname(dest_path)
    if dir_dest_path == "":
        os.makedirs(dir_dest_path, exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(template)

    print("Done")


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block[2:].strip()
    raise Exception("Missing h1")
