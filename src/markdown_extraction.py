from textnode import TextType
from leafnode import LeafNode
import re 

# add some error / None handling
def extract_markdown_images(text):
    if isinstance(text, str):
        images = []
        matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
        for match in matches:
            images.append(match)
        return images
    else:
        raise TypeError("Input must be a string")
    
def extract_markdown_links(text):
    if isinstance(text, str):
        links = []
        matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
        for match in matches:
            links.append(match)
        return links 
    else:
        raise TypeError("Input must be a string")