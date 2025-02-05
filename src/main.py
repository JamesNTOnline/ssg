from textnode import TextNode, TextType
from node_converter import markdown_to_html_node
from markdown_extraction import extract_markdown_title
import os
import shutil

def copy_static(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        raise Exception(f"Source directory '{src_dir}' does not exist")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)
    contents = os.listdir(src_dir)
    for item in contents:
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            copy_static(src_path, dest_path)
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path}")
    markdown = read_file(from_path)
    template = read_file(template_path)
    html = markdown_to_html_node(markdown).to_html()
    title = extract_markdown_title(markdown)
    page = process_template(template, html, title)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(page)
    
def read_file(path):
    if not os.path.exists(path):
        raise Exception(f"File '{path}' does not exist")
    with open(path, "r") as f:
        return f.read()    

def process_template(template, content, title):
    return template.replace("{{ Content }}", content).replace("{{ Title }}", title)


def main():
    node_one = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node_one)
    copy_static("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")
    

if __name__ == "__main__":
    main()