from textnode import TextType
from leafnode import LeafNode
import re 

def extract_markdown_images(text):
    images = []
    matches = text.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)")
    for match in matches:
        images.append(LeafNode(TextType.IMAGE, match[0], match[1]))
    
def extract_markdown_links(text)
    links = []
    matches = text.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)")
    for match in matches:
        images.append(LeafNode(TextType.IMAGE, match[0], match[1]))