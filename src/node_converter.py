from textnode import TextType, TextNode
from leafnode import LeafNode
from parentnode import ParentNode
from node_splitter import *
from markdown_extraction import *
import re


def text_node_to_html_node(text_node):
    """
    converts a TextNode to a LeafNode (HTMLNode)
    args:
        text_node (TextNode): a TextNode object
    returns:
        LeafNode: a LeafNode object
    """
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", props={
            "src": text_node.url,
            "alt": text_node.text
        })
    raise ValueError("Unknown text type")



def text_to_textnodes(text):
    """
    Splits a text into text nodes based on inline markdown formatting
    Args:
        text (str): a piece of markdown text to split into nodes
    Returns:
        list: list of TextNodes.
    """
    new_nodes = [TextNode(text, TextType.TEXT)]
    delimiters = [("**", TextType.BOLD), ("*", TextType.ITALIC), ("`", TextType.CODE)]
    for d in delimiters:
        new_nodes = split_formatted_nodes(new_nodes, *d)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes


def block_to_block_type(text):
    lines = text.split("\n") # need to check for lists 
    if re.match(r"^#{1,6} ", text):
        return "heading"
    # what if there are multiple code blocks?
    if text.startswith("```") and text.endswith("```"):
        return "code"
    if all(line.startswith("* ") for line in lines) or all(line.startswith("- ") for line in lines):
        return "unordered list"
    if all(line.startswith("> ") for line in lines):
        return "quote"
    if text.startswith("1. "):
        for i, line in enumerate(lines, start=1):
            if not line.startswith(f"{i}. "):
                return "paragraph"
        return "ordered list"
    return "paragraph"
    
    
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    page_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "paragraph":
            page_nodes.append(paragraph_to_html_node(block))
        if block_type == "heading":
            page_nodes.append(header_block_to_html_node(block))
        if block_type == "code":
            page_nodes.append(code_block_to_html_node(block))
        if block_type == "quote":
            page_nodes.append(quote_block_to_html_node(block))
        if block_type == "ordered list" or block_type == "unordered list":
            page_nodes.append(list_block_to_html_nodes(block))
    return ParentNode("div", page_nodes)

def paragraph_to_html_node(block):
    child_nodes = text_to_children(block)
    return ParentNode("p", child_nodes)

def header_block_to_html_node(block):
    header_md = block.split(" ", 1)
    level = len(header_md[0]) if len(header_md[0]) <= 6 else 6
    contents = header_md[1]
    child_nodes = text_to_children(contents)    
    return ParentNode(f"h{level}", child_nodes)

def code_block_to_html_node(block):
    code = block[3:-3]
    code_node = LeafNode("code", code)
    return ParentNode("pre", [code_node])

def quote_block_to_html_node(block):
    contents = block.replace("\n>", "\n").lstrip(">")
    child_nodes = text_to_children(contents)
    return ParentNode("blockquote", child_nodes)

def list_block_to_html_nodes(block):
    tag = "ul" if block.startswith("*") else "ol"
    list_nodes = []
    lines = block.split("\n")
    # splits each line into its markdown and content, then strips the content in [1] to use for the list of items
    contents = [line.split(" ", 1)[1].strip() for line in lines]
    for item in contents:
        child_nodes = text_to_children(item)
        list_nodes.append(ParentNode("li", child_nodes))
    return ParentNode(tag, list_nodes)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children