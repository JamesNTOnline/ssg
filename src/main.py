from textnode import TextNode, TextType
from node_converter import markdown_to_html_node
from markdown_extraction import extract_markdown_title
import os
import shutil
from pathlib import Path

def copy_static(src_dir, dest_dir):
    src = Path(src_dir)
    dest = Path(dest_dir)
    if not src.exists():
        raise Exception(f"Source directory '{src}' does not exist")
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir()
    for item in src.iterdir():
        dest_path = dest / item.name
        if item.is_file():
            shutil.copy(item, dest_path)
        else:
            copy_static(item, dest_path)
 
def read_file(path):
    path = Path(path)
    if not path.exists():
        raise Exception(f"File '{path}' does not exist")
    return path.read_text()    

def process_template(template, content, title):
    return template.replace("{{ Content }}", content).replace("{{ Title }}", title) 
    
def generate_page(from_path, template_path, dest_path):
    from_path = Path(from_path)
    template_path = Path(template_path)
    dest_path = Path(dest_path)
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    markdown = read_file(from_path)
    template = read_file(template_path)
    html = markdown_to_html_node(markdown).to_html()
    title = extract_markdown_title(markdown)
    page = process_template(template, html, title)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(page)

def generate_pages_recursive(dir_path_cntnt, template_path, dest_dir_path):
    dir_path = Path(dir_path_cntnt)
    dest_dir = Path(dest_dir_path)
    dest_dir.mkdir(parents=True, exist_ok=True)
    for item in dir_path.iterdir():
        if item.is_dir():
            new_dest = dest_dir / item.name
            new_dest.mkdir(parents=True, exist_ok=True)
            generate_pages_recursive(item, template_path, new_dest)
        elif item.suffix == '.md':
            new_dest = dest_dir / item.with_suffix('.html').name
            generate_page(str(item), template_path, str(new_dest))

def main():
    node_one = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node_one)
    copy_static("static", "public")
    generate_pages_recursive("content", "template.html", "public")
    

if __name__ == "__main__":
    main()