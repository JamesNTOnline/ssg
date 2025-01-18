import unittest 
import test_setup 
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def setUp(self):
        
        self.parent_simple = ParentNode("p", [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ])

        self.parent_child_no_value = ParentNode("div", [
            LeafNode("p", "This is a paragraph.", {"class": "text"}),
            LeafNode("img", props={"src": "image.jpg", "alt": "An image"})
        ], {"class": "container"})

        self.parent_child_no_props = ParentNode("section", [
            LeafNode("h1", "Main Title"),
            LeafNode("p", "Another paragraph.", {"class": "text"})
        ], {"id": "main-section"})

        self.parent_child_parent = ParentNode("article", [
            LeafNode("h2", "Article Title"),
            self.parent_child_no_value  # Nested parent node
        ])

        self.parent_nested_parents = ParentNode("div", [
            self.parent_child_no_value,  # Nested parent node
            self.parent_child_no_props   # Nested parent node
        ], {"class": "wrapper"})
        
    def test_parent_simple(self):
        self.assertEqual(self.parent_simple.to_html(),
                            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
    
    def test_parent_child_no_value(self):
        self.assertEqual(self.parent_child_no_value.to_html(),
                            "<div class='container'><p class='text'>This is a paragraph.</p><img src='image.jpg' alt='An image'/></div>")
    
    def test_parent_child_no_props(self):
        self.assertEqual(self.parent_child_no_props.to_html(),
                            "<section id='main-section'><h1>Main Title</h1><p class='text'>Another paragraph.</p></section>")
        
    def test_parent_child_parent(self):
        self.assertEqual(self.parent_child_parent.to_html(),
                            "<article><h2>Article Title</h2><div class='container'><p class='text'>This is a paragraph.</p><img src='image.jpg' alt='An image'/></div></article>")
        
    def test_parent_nested_parents(self):
        self.assertEqual(self.parent_nested_parents.to_html(),
                            "<div class='wrapper'><div class='container'><p class='text'>This is a paragraph.</p><img src='image.jpg' alt='An image'/></div><section id='main-section'><h1>Main Title</h1><p class='text'>Another paragraph.</p></section></div>")


if __name__ == "__main__":
    unittest.main()
