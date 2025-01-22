import unittest 
import test_setup 
from node_splitter import split_formatted_nodes, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

class TestNodeSplitter(unittest.TestCase):
    
    def test_split_with_paired_delimiters(self):
        old_nodes = [TextNode("This `is text` with a `code block` word", TextType.TEXT)]
        new_nodes = split_formatted_nodes(old_nodes, "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 5)
        
    def test_split_with_unpaired_delimiters(self):
        unclosed_nodes = [TextNode("This `is text` with a `code block word", TextType.TEXT)]
        with self.assertRaises(Exception, msg="Unpaired delimiter found, invalid Markdown"):
            split_formatted_nodes(unclosed_nodes, "`", TextType.CODE)
        
    def test_multiple_calls(self):
        node = [TextNode("This is **BOLD** text with a `code block`", TextType.TEXT)]
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("BOLD", TextType.BOLD),
            TextNode(" text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode("", TextType.TEXT)
        ]
        actual = split_formatted_nodes(node, "**", TextType.BOLD)
        actual = split_formatted_nodes(actual, "`", TextType.CODE)
        self.assertEqual(len(actual), len(expected))
        for i in range(len(expected)):
            self.assertEqual(actual[i].text, expected[i].text)
            self.assertEqual(actual[i].text_type, expected[i].text_type)
    
    
    def test_split_image(self):
        node = TextNode("Here's a ![cat](cat.png) and a ![dog](dog.png)", TextType.TEXT)
        expected = [
            TextNode("Here's a ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "cat.png"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("dog", TextType.IMAGE, "dog.png")
        ]
        actual = split_nodes_image([node])
        self.assertEqual(len(actual), len(expected))
        for i in range(len(expected)):
            self.assertEqual(actual[i].text, expected[i].text)
            self.assertEqual(actual[i].text_type, expected[i].text_type)
            if expected[i].url:
                self.assertEqual(actual[i].url, expected[i].url)
        

    def test_split_link(self):
        node = TextNode("This is text with a link [to twitter](https://x.com) and [to google](https://www.google.com/)", TextType.TEXT)
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to twitter", TextType.LINK, "https://x.com"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to google", TextType.LINK, "https://www.google.com/")
        ]  
        actual = split_nodes_link([node])
        self.assertEqual(len(actual), len(expected))
        for i in range(len(expected)):
            self.assertEqual(actual[i].text, expected[i].text)
            self.assertEqual(actual[i].text_type, expected[i].text_type)
            if expected[i].url:
                self.assertEqual(actual[i].url, expected[i].url)
                
    def test_split_image_and_link(self):
        node = TextNode("Here's a ![cat](cat.png) and a link [to twitter](https://x.com)", TextType.TEXT)
        expected = [
            TextNode("Here's a ", TextType.TEXT),
            TextNode("cat", TextType.IMAGE, "cat.png"),
            TextNode(" and a link ", TextType.TEXT),
            TextNode("to twitter", TextType.LINK, "https://x.com")
        ]
        actual = split_nodes_image([node])
        actual = split_nodes_link(actual)
        self.assertEqual(len(actual), len(expected))
        for i in range(len(expected)):
            self.assertEqual(actual[i].text, expected[i].text)
            self.assertEqual(actual[i].text_type, expected[i].text_type)
            if expected[i].url:
                self.assertEqual(actual[i].url, expected[i].url)
