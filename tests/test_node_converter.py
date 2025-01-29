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
    
    
    # testing paragraph md to html conversion
    def test_paragraph_block_to_html_node(self):
        text = "This is a paragraph"
        expected = ParentNode("p", [
            LeafNode(None, "This is a paragraph")
        ]).to_html()
        actual = paragraph_to_html_node(text).to_html()
        self.assertEqual(expected, actual)
    
    def test_paragraph_with_formatted_text(self):
        text = "This is a paragraph with **bold text** and *italic words*"
        expected = ParentNode("p", [
            LeafNode(None, "This is a paragraph with "),
            ParentNode("b", [
                LeafNode(None, "bold text")
            ]),
            LeafNode(None, " and "),
            ParentNode("i", [
                LeafNode(None, "italic words")
            ])
        ]).to_html()
        actual = paragraph_to_html_node(text).to_html()
        self.assertEqual(expected, actual)
    
    # testing header md to html conversion
    def test_header_block_to_html_node(self):
        text = "# Heading"
        expected = ParentNode("h1", [
            LeafNode(None, "Heading")
        ]).to_html()
        actual = header_block_to_html_node(text).to_html()
        self.assertEqual(expected, actual)
    
    def test_header_with_formatted_text(self):
        text = "## Heading with **bold text** and *italic words*"
        expected = ParentNode("h2", [
            LeafNode(None, "Heading with "),
            ParentNode("b", [
                LeafNode(None, "bold text")
            ]),
            LeafNode(None, " and "),
            ParentNode("i", [
                LeafNode(None, "italic words")
            ])
        ]).to_html()
        actual = header_block_to_html_node(text).to_html()
        self.assertEqual(expected, actual)
    
    # testing list md to html list conversion 
    def test_ul_block_to_html_node(self):
        text = "* First item\n* Second item\n* Third item"
        expected = ParentNode("ul", [
            ParentNode("li", [
                LeafNode(None, "First item")
            ]),
            ParentNode("li", [
                LeafNode(None, "Second item")
            ]),
            ParentNode("li", [
                LeafNode(None, "Third item")
            ])
        ]).to_html()
        actual = list_block_to_html_nodes(text).to_html()
        self.assertEqual(expected, actual)
        
    def test_ul_block_with_empty_items(self):
        text = "* First item\n* \n* Third item"
        expected = ParentNode("ul", [
            ParentNode("li", [
                LeafNode(None, "First item")
            ]),
            ParentNode("li", [
                LeafNode(None, "")
            ]),
            ParentNode("li", [
                LeafNode(None, "Third item")
            ])
        ]).to_html()
        actual = list_block_to_html_nodes(text).to_html()
        self.assertEqual(expected, actual)
        
    def test_list_with_formatted_text(self):
        text = "* Item with **bold text**\n* Item with *italic words*"
        expected = ParentNode("ul", [
            ParentNode("li", [
                LeafNode(None, "Item with "),
                ParentNode("b", [
                    LeafNode(None, "bold text")
                ])
            ]),
            ParentNode("li", [
                LeafNode(None, "Item with "),
                ParentNode("i", [
                    LeafNode(None, "italic words")
                ])
            ])
        ]).to_html()
        actual = list_block_to_html_nodes(text).to_html()
        self.assertEqual(expected, actual)
        
    def test_ol_block_to_html_node(self):
        text = "1. First item\n2. Second item\n3. Third item"
        expected = ParentNode("ol", [
            ParentNode("li", [
                LeafNode(None, "First item")
            ]),
            ParentNode("li", [
                LeafNode(None, "Second item")
            ]),
            ParentNode("li", [
                LeafNode(None, "Third item")
            ])
        ]).to_html()
        actual = list_block_to_html_nodes(text).to_html()
        self.assertEqual(expected, actual)
        
    def test_ol_block_with_two_digit_numbers(self):
        text = "9. Ninth\n10. Tenth\n11. Eleventh"
        expected = ParentNode("ol", [
            ParentNode("li", [
                LeafNode(None, "Ninth")
            ]),
            ParentNode("li", [
                LeafNode(None, "Tenth")
            ]),
            ParentNode("li", [
                LeafNode(None, "Eleventh")
            ])
        ]).to_html()
        actual = list_block_to_html_nodes(text).to_html()
        self.assertEqual(expected, actual)

    # testing quote md to html conversion
    def test_quote_block_to_html(self):
        text = ">First line\n>Second line"
        expected = ParentNode("blockquote", [
            LeafNode(None, "First line\nSecond line")
        ]).to_html()
        actual = quote_block_to_html_node(text).to_html()
        self.assertEqual(expected, actual)

    def test_quote_block_with_formatted_text(self):
        text = ">First line with **bold text**\n>Second line with *italic words*"
        expected = ParentNode("blockquote", [
            LeafNode(None, "First line with "),
            ParentNode("b", [
                LeafNode(None, "bold text")
            ]),
            LeafNode(None, "\nSecond line with "),
            ParentNode("i", [
                LeafNode(None, "italic words")
            ])
        ]).to_html()
        actual = quote_block_to_html_node(text).to_html()
        self.assertEqual(expected, actual)
    
    # testing code md to html conversion
    def test_code_block_to_html_node(self):
        text = "```\ndef hello():\n    print('Hello!')\n```"
        expected = ParentNode("pre", 
            [LeafNode("code", "\ndef hello():\n    print('Hello!')\n")]).to_html()
        actual = code_block_to_html_node(text).to_html()
        self.assertEqual(expected, actual)
    
    def test_code_block_with_markdown_characters(self):
        text = "```\ndef hello():\n    print('*italic text*')\n    return '**bold text**'\n```"
        expected = ParentNode("pre", 
            [LeafNode("code", "\ndef hello():\n    print('*italic text*')\n    return '**bold text**'\n")]).to_html()
        actual = code_block_to_html_node(text).to_html()
        self.assertEqual(expected, actual)
    
    # testing markdown to html conversion
    def test_markdown_to_html_node_with_formatting_and_image(self):
        markdown = (
            "# Heading\n\n"
            "This is a **bold** paragraph with an ![An image](image.png)\n\n"
            "* List item 1\n"
            "* List item 2"
        )
        expected = ParentNode("div", [
            ParentNode("h1", [
                LeafNode(None, "Heading")
            ]),
            ParentNode("p", [
                LeafNode(None, "This is a "),
                ParentNode("b", [
                    LeafNode(None, "bold")
                ]),
                LeafNode(None, " paragraph with an "),
                LeafNode("img", "", {"src": "image.png", "alt": "An image"})
            ]),
            ParentNode("ul", [
                ParentNode("li", [
                    LeafNode(None, "List item 1")
                ]),
                ParentNode("li", [
                    LeafNode(None, "List item 2")
                ])
            ])
        ]).to_html()
        actual = markdown_to_html_node(markdown).to_html()
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