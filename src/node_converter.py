from textnode import TextType, TextNode
from leafnode import LeafNode
from node_splitter import split_formatted_nodes, split_nodes_image, split_nodes_link

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