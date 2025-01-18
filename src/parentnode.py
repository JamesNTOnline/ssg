from htmlnode import HTMLNode


"""
ParentNode an HTML node that can have children and handles their rendering
"""
class ParentNode(HTMLNode):
    
    def __init__(self, tag, children, props=None):
        """
        Initializes a ParentNode instance.
        Args:
            tag (str, optional): The HTML tag name (e.g., 'div'). Defaults to None.
            children (list, optional): A list of HTMLNode instances that are children of the ParentNode. Defaults to None.
            props (dict, optional): A dictionary of key-value pairs representing the attributes of the HTML tag, e.g., {"class": "container"} for a <div> tag. Defaults to None.
        """
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be None")
        if self.children is None:
            raise ValueError("Parent node must have children")
        return f"<{self.tag}{self.props_to_html()}>{''.join([child.to_html() for child in self.children])}</{self.tag}>"
        