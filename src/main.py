import os
import shutil

from copystatic import copy_assets
from generatepage import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
template_path = "./template.html"
content_path = "./content"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    copy_assets(dir_path_static, dir_path_public)

    index_path = os.path.join(content_path, "index.md")
    dest_path = os.path.join(dir_path_public, "index.html")

    generate_page(index_path, template_path, dest_path)


main()
