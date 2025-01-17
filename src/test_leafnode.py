import unittest 

from leafnode import LeafNode

class TestTextNode(unittest.TestCase):
    def setUp(self):
        self.leaf_no_value = LeafNode("p", None)
        self.leaf_no_tag = LeafNode(None, "Hola, mundo!")
        self.leaf_no_tag_empty_value = LeafNode(None, "")
        self.leaf_no_props = LeafNode("p", "This is a paragraph of text.")
        self.leaf_one_prop = LeafNode("a", "Click here", {'href': 'https://example.com'})
        self.leaf_two_prop = LeafNode("img", "", {"src": "image.png", "alt": "An image"})

    def test_leaf_no_value(self):
        with self.assertRaises(ValueError): # python's context manager 
            self.leaf_no_value.to_html() # testing ValueError is raised when to_html() is called

    def test_leaf_no_tag(self):
        self.assertEqual(self.leaf_no_tag.to_html(), "Hola, mundo!")
        
    def test_leaf_no_tag_empty_value(self):
        self.assertEqual(self.leaf_no_tag_empty_value.to_html(), "")
    
    def test_leaf_no_props(self):
        self.assertEqual(self.leaf_no_props.to_html(), "<p>This is a paragraph of text.</p>")
        
    def test_leaf_with_props(self):
        self.assertEqual(self.leaf_one_prop.to_html(), "<a href='https://example.com'>Click here</a>")

    def test_leaf_with_two_props(self):
        self.assertEqual(self.leaf_two_prop.to_html(), "<img src='image.png' alt='An image'/>")

        
    
    
if __name__ == "__main__":
    unittest.main()
