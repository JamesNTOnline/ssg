from textnode import TextType, TextNode
from markdown_extraction import extract_markdown_images, extract_markdown_links


def split_formatted_nodes(old_nodes, delimiter, text_type):
    """
    Splits a list of nodes based on a given delimiter and text type
    Args:
        old_nodes (list): List of nodes to be split 
        delimiter (str): Delimiter to split nodes on
        text_type (str): The type of text the new node should be
    Returns:
        list: A new list of nodes after splitting based on the delimiter and text type
    """
    new_nodes = [] 
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            # an even number of parts means that the delimiter is unpaired
            # an odd number of parts means that the delimiter is paired
            # e.g. "Hello **world**" -> ["Hello ", "world", ""]
            if len(parts) % 2 == 0:
                raise Exception("Unpaired delimiter found, invalid Markdown")
            else:
                for i, part in enumerate(parts):
                    node_type = TextType.TEXT if i % 2 == 0 else text_type
                    new_nodes.append(TextNode(part, node_type))
        else:
            new_nodes.append(node)
    return new_nodes
    



def split_nodes_image(old_nodes):
    """
    Splits a list of nodes and extracts images from text nodes.
    Args:
        old_nodes (list): List of nodes to be split
    Returns:
        list: A new list of nodes with image nodes extracted from text nodes
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            images = extract_markdown_images(node.text)
            parts = node.text
            if images: 
                for image in images:
                    parts = parts.split(f"![{image[0]}]({image[1]})", 1)
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                    new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                    parts = parts[1]
                if not parts == "":
                    new_nodes.append(TextNode(parts, TextType.TEXT))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            links = extract_markdown_links(node.text)
            parts = node.text
            if links:
                for link in links:
                    parts = parts.split(f"[{link[0]}]({link[1]})", 1)
                    new_nodes.append(TextNode(parts[0], TextType.TEXT))
                    new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                    parts = parts[1]
                if not parts == "":
                    new_nodes.append(TextNode(parts, TextType.TEXT))
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes