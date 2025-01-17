

class HTMLNode:
    """Base class for HTML nodes in a document tree.
    
    Attributes:
        tag: The HTML tag name
        props: HTML attributes as key-value pairs
    """

    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Initializes an HTMLNode instance.
        Args:
            tag (str, optional): The HTML tag name (e.g., 'p'). Defaults to None.
            value (str, optional): The value of the HTML tag, e.g., text inside a paragraph. Defaults to None.
            children (list, optional): A list of HTMLNode objects that are children of this node. Defaults to None.
            props (dict, optional): A dictionary of key-value pairs representing the attributes of the HTML tag, e.g., {"href": "https://example.com"} for an <a> tag. Defaults to None.
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self): # child classes should override this method
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return " " +" ".join([f"{key}='{value}'" for key, value in self.props.items()])

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
