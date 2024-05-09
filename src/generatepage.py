import os
import re
from pathlib import Path

from block_markdown import markdown_to_html_node, markdown_to_blocks


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)


# def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
#     _gen_pages_rec(dir_path_content, template_path, dest_dir_path, "")
#
#
# def _gen_pages_rec(base, template_path, dest_dir_path, cur_path=""):
#     print("base", base)
#     print("cur_path", cur_path)
#     file_list = os.listdir(os.path.join(base, cur_path))
#     for file in file_list:
#         file_path = os.path.join(base, cur_path, file)
#         print("process", file_path)
#         path = pathlib.Path(file_path)
#         print("process", path)
#         if os.path.isfile(file_path) and path.suffix == ".md":
#             dest_path = os.path.join(
#                 dest_dir_path, path.with_suffix(".html").relative_to(base)
#             )
#
#             generate_page(file_path, template_path, dest_path)
#         elif os.path.isdir(file_path):
#             print("dir", file_path)
#             _gen_pages_rec(
#                 base, template_path, dest_dir_path, os.path.join(cur_path, file)
#             )
#         else:
#             raise Exception(f"{file_path} is not valid")


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

    dir_dest_path = os.path.dirname(dest_path)
    if not os.path.exists(dir_dest_path):
        os.makedirs(dir_dest_path, exist_ok=True)

    print(f"Writing to {dest_path}")
    with open(dest_path, "w", encoding="utf-8") as file:
        file.write(template)

    print("Done")


def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block.startswith("# "):
            return block[2:].strip()
    raise Exception("Missing h1")
