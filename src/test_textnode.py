import unittest 

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def setUp(self):
        self.node_bold_one = TextNode("This is a text node", TextType.BOLD)
        self.node_bold_two = TextNode("This is a text node", TextType.BOLD)
        self.node_italic = TextNode("This is a text node", TextType.ITALIC)
        self.node_invalid = "Not a TextNode"
        self.node_url = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    
    
    def test_eq_same_text(self):
        self.assertEqual(self.node_bold_one, self.node_bold_two)

    def test_eq_different_type(self):
        self.assertNotEqual(self.node_bold_one, self.node_italic)
        
    def test_eq_different_args(self):
        self.assertNotEqual(self.node_bold_one, self.node_url)
    
    def test_eq_non_node(self):
        self.assertNotEqual(self.node_bold_one, self.node_invalid)

if __name__ == "__main__":
    unittest.main()
