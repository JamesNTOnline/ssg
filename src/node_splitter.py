from textnode import TextType, TextNode


def split_nodes(old_nodes, delimiter, text_type):
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
                #nodes_to_add = []
                for i, part in enumerate(parts):
                    node_type = TextType.TEXT if i % 2 == 0 else text_type
                    new_nodes.append(TextNode(part, node_type))
           
           # text = node.text
            #while True:
               # start = text.find(delimiter)
                #if start != -1: #  delimiter found
                    #end = start + len(delimiter) # find where the text starts
                    # find the closing delimiter 
                    # make a node from the text in between
                    # ???
            
            
        else:
            new_nodes.append(node)
    return new_nodes
            