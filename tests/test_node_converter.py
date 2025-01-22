import unittest
import test_setup 
from node_converter import text_node_to_html_node, text_to_textnodes
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
    
    
if __name__ == "__main__":
    unittest.main()