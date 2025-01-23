import unittest
import test_setup 
from node_converter import *
from textnode import TextNode, TextType


class TestNodeConverter(unittest.TestCase):

    def test_text_node(self):
        self.text_node = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(text_node_to_html_node(self.text_node).to_html(), "This is a text node")


    def test_bold_node_to_html_node(self):
        self.text_node_bold = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual(text_node_to_html_node(self.text_node_bold).to_html(), "<b>This is a text node</b>")

        
    def test_italic_node_to_html(self):
        self.text_node_italic = TextNode("This is an italic text node", TextType.ITALIC, "https://www.example.com")
        self.assertEqual(text_node_to_html_node(self.text_node_italic).to_html(), "<i>This is an italic text node</i>")
  
    
    def test_invalid_text_node_to_html(self):
        class InvalidTextType:
            UNDERLINE = "underline"
        self.text_node_underline = TextNode("This is an underline text node", InvalidTextType.UNDERLINE, "https://www.sample.com")
        with self.assertRaises(ValueError):
            text_node_to_html_node(self.text_node_underline)
        
    def test_text_to_textnode_bold(self):
        text = "This is a **bold** text"
        expected = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)   
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(expected, actual)
    
    
    # tests for blocks to html nodes 
    def test_block_to_html_node_list(self):
        text = "* This is a test\n* This is **bold** text\n* Here's *italic* text"
        expected = ParentNode("ul", [
            ParentNode("li", [
                LeafNode(None, "This is a test")
            ]),
            ParentNode("li", [
                LeafNode(None, "This is "),
                ParentNode("b", [
                    LeafNode(None, "bold")
                ]),
                LeafNode(None, " text")
            ]),
            ParentNode("li", [
                LeafNode(None, "Here's "),
                ParentNode("i", [
                    LeafNode(None, "italic")
                ]),
                LeafNode(None, " text")
            ])
        ]).to_html()
        actual = list_block_to_html_nodes(text).to_html()
        self.assertEqual(expected, actual)
    
    # block to type testing
    def test_block_to_block_type_heading_1(self):
        text = "# Heading"
        self.assertEqual(block_to_block_type(text), "heading")
        
    def test_block_to_block_type_heading_6(self):
        text = "###### Heading"
        self.assertEqual(block_to_block_type(text), "heading")
        
    def test_block_to_type_invalid_heading(self):
        text = "####### Invalid heading"
        self.assertEqual(block_to_block_type(text), "paragraph")
    
    def test_block_to_block_type_code(self):
        text = "```python\nprint('Hello, World!')\n```"
        self.assertEqual(block_to_block_type(text), "code")
        
    def test_block_to_block_type_unordered_list(self):
        text = "* List item 1\n* List item 2"
        self.assertEqual(block_to_block_type(text), "unordered list")
        
    def test_block_to_block_type_quote(self):
        text = "> This is a quote"
        self.assertEqual(block_to_block_type(text), "quote")
        
    def test_block_to_block_type_ordered_list(self):
        text = "1. List item 1\n2. List item 2"
        self.assertEqual(block_to_block_type(text), "ordered list")
    
    def test_block_to_block_type_paragraph(self):
        text = "This is a paragraph"
        self.assertEqual(block_to_block_type(text), "paragraph")
    
    def test_block_to_block_type_invalid_ordered_list(self):
        text = "1. List item 1\n3. List item 2"
        self.assertEqual(block_to_block_type(text), "paragraph")
    
    def test_block_to_block_type_invalid_unordered_list(self):
        text = "* List item 1\n- List item 2"
        self.assertEqual(block_to_block_type(text), "paragraph")
    
    def test_block_to_block_type_invalid_quote(self):
        text = "> This is a quote\nThis is a paragraph"
        self.assertEqual(block_to_block_type(text), "paragraph")


if __name__ == "__main__":
    unittest.main()