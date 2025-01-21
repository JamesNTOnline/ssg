import unittest 
import test_setup 
from node_splitter import split_nodes
from textnode import TextNode, TextType

class TestNodeSplitter(unittest.TestCase):
    
    def test_split_with_paired_delimiters(self):
        old_nodes = [TextNode("This `is text` with a `code block` word", TextType.TEXT)]
        new_nodes = split_nodes(old_nodes, "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 5)
        
    def test_split_with_unpaired_delimiters(self):
        unclosed_nodes = [TextNode("This `is text` with a `code block word", TextType.TEXT)]
        with self.assertRaises(Exception, msg="Unpaired delimiter found, invalid Markdown"):
            split_nodes(unclosed_nodes, "`", TextType.CODE)
        
    def test_multiple_calls(self):
        old_nodes = [TextNode("This is **BOLD** text with a `code block`", TextType.TEXT)]
        new_nodes = split_nodes(old_nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        new_nodes = split_nodes(new_nodes, "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[1].text, "BOLD")
        self.assertEqual(new_nodes[2].text, " text with a ")
        self.assertEqual(new_nodes[3].text, "code block")
        self.assertEqual(new_nodes[4].text, "")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[3].text_type, TextType.CODE)
        self.assertEqual(new_nodes[4].text_type, TextType.TEXT)


