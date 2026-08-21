import os
from pathlib import Path
import shutil
from functions import markdown_to_html_node
from htmlnode import *

def CopyStatic() -> None:
    dir = Path(__file__).resolve().parent.parent / "public"

    if Path(dir).exists():
        shutil.rmtree(dir) #delete directory; does not return anything

        if Path(dir).exists():
            raise Exception('"public" directory not deleted')

    if not Path(dir).exists(): #make new directory
        os.mkdir(dir) #does not return anything

    source_dir = Path(__file__).resolve().parent.parent / "static"
    shutil.copytree(source_dir, dir, dirs_exist_ok=True)

def extract_title(markdown: str) -> str:
    h1: str = ""
    i = 0

    while i < len(markdown) and markdown[i] != "#":
        i += 1

    if i+1 < len(markdown) and markdown[i] == "#" and markdown[i+1] == " ":
        i += 2
        while i < len(markdown) and markdown[i] != "\n":
            h1 += markdown[i]
            i += 1
    else:
        raise Exception ("h1 header does not exist.")
    return h1.strip()

def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    try:
        file = open(from_path, mode='r')
    except OSError as e:
        raise Exception("Unable to open file")
    md: str = file.read()
    file.close()

    try:
        file = open(template_path, mode='r')
    except OSError as e:
        raise Exception("Unable to open template file")
    template: str = file.read()
    file.close()

    #convert markdown to html string
    node = markdown_to_html_node(md)
    html: str = node.to_html()

    title: str = extract_title(md)

    #replace title and html content placeholders in template with values extracted above
    new_page:str = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    dest_path = Path(dest_path)

    if dest_path.exists() and dest_path.is_file():
        dest_path.unlink() #delete file

    if not dest_path.exists():
        dest_path.write_text(new_page)

    
