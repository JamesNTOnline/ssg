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
    
def markdown_to_blocks(markdown):
    """
    Break a markdown document into a list of text blocks
    
    Returns:
        list: Text blocks extracted from the raw string

    Raises:
        TypeError: If the input is not a string.
    """
    if isinstance(markdown, str):
        blocks = []
        lines = re.split(r"\n\s*\n\s*", markdown)
        for line in lines:
            blocks.append(line.strip())
        return blocks
    else:
        raise TypeError("Input must be a string")