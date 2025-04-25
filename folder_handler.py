import os

def get_files_within_folder(folder: str) -> list:
    files = []
    for file in os.listdir(folder):
        if(file.split('.')[-1] == 'csv'):
            files.append(folder + file)

    return files


def extract_name(filename: str) -> str:

    base = os.path.basename(filename)

    name, _ = os.path.splitext(base)
    return name