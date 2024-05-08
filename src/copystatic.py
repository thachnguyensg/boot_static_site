import os
import shutil


def copy_assets(source, destination):
    print(f"Copying assets {source} to {destination}")
    if not os.path.exists(source):
        raise Exception(f"Source directory {source} does not exist")
    if not os.path.exists(destination):
        os.mkdir(destination)

    if os.path.isdir(source):
        file_list = get_files(source)
        for path, files in file_list.items():
            source_path = os.path.join(source, path)
            dest_path = os.path.join(destination, path)
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            for file in files:
                source_file = os.path.join(source_path, file)
                dest_file = os.path.join(dest_path, file)
                print(f"copy {source_file} to {dest_file}")
                shutil.copy(source_file, dest_file)

    print("Assets copied")


def get_files(source, current_path=""):
    source_files = os.listdir(source)
    file_list = {}
    files = []
    for file in source_files:
        file_path = os.path.join(source, file)
        if os.path.isdir(file_path):
            file_list.update(get_files(file_path, os.path.join(current_path, file)))
        else:
            files.append(file)
    file_list[current_path] = files
    return file_list
