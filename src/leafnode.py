from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):
        """
        Initializes a LeafNode instance.
        Args:
            tag (str, optional): The HTML tag name (e.g., 'p'). Defaults to None.
            value (str, optional): The value of the HTML tag, e.g., text inside a paragraph. Defaults to None.
            props (dict, optional): A dictionary of key-value pairs representing the attributes of the HTML tag, e.g., {"href": "https://example.com"} for an <a> tag. Defaults to None.
        """
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Value cannot be None")
        if self.tag == None:
            return self.value 