
import unittest 
import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def setUp(self):
        self.node = HTMLNode(tag='p', value='Hello, World!', children=None, props={'class': 'text'})


    def test_initialization(self):
        self.assertEqual(self.node.tag, 'p')
        self.assertEqual(self.node.value, 'Hello, World!')
        self.assertIsNone(self.node.children)
        self.assertEqual(self.node.props, {'class': 'text'})

    def test_props_to_html(self):
        self.assertEqual(self.node.props_to_html(), "class='text'")

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag='p', value='Hello, World!')
        self.assertEqual(node.props_to_html(), "")

    def test_to_html_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            self.node.to_html()

    def test_repr(self):
        self.assertEqual(repr(self.node), "HTMLNode(p, Hello, World!, None, {'class': 'text'})")

if __name__ == "__main__":
    unittest.main()