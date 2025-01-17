from htmlnode import HTMLNode


"""
ParentNode an HTML node that can have children and handles their rendering
"""
class ParentNode(HTMLNode):
    
    def __init__(self, tag, value, props=None):