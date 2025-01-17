from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    # self closing tags need different handling 
    VOID_ELEMENTS = frozenset(["br", "hr", "img"]) # frozense is immutable
    
    def __init__(self, tag, value, props=None):
        """
        Initializes a LeafNode instance.
        Args:
            tag (str, optional): The HTML tag name (e.g., 'p'). Defaults to None.
            value (str, optional): The value of the HTML tag, e.g., text inside a paragraph. Defaults to None.
            props (dict, optional): A dictionary of key-value pairs representing the attributes of the HTML tag, e.g., {"href": "https://example.com"} for an <a> tag. Defaults to None.
        """
        super().__init__(tag, value, None, props)
        
    # should void elements have a value?
    # br and img behave differently - br never has a value, img might have attributes
    # wont deal with this for now, but something to think about
    def to_html(self):
        #print(f"Tag: {self.tag}, Is void: {self.tag in self.VOID_ELEMENTS}")  # debug
        if self.value is None: # what about "" - empty string? <br> doesn't have a value
            raise ValueError("Value cannot be None")
        elif self.tag is None:
            return self.value
        elif self.tag in self.VOID_ELEMENTS:
            return f"<{self.tag}{self.props_to_html()}/>" #format self closing tags differently
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"