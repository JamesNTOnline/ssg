from textnode import TextType, TextNode
from leafnode import LeafNode
from parentnode import ParentNode
from node_splitter import *
from markdown_extraction import *
import re


def text_node_to_html_node(text_node):
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
    
    
def block_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    
    for block in blocks:
        block_type = block_to_block_type(block)


def list_block_to_html_nodes(block):
    tag = "ul" if block.startswith("*") else "ol"
    list_nodes = []
    lines = block.split("\n")
    items = [line[2:] for line in lines]
    for item in items:
        child_nodes = []
        text_nodes = text_to_textnodes(item)
        for node in text_nodes:
            child_nodes.append(text_node_to_html_node(node))
        list_nodes.append(ParentNode("li", child_nodes))
    return ParentNode(tag, list_nodes)


def text_to_child_nodes(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]