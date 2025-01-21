import unittest 
import test_setup 
from markdown_extraction import extract_markdown_images, extract_markdown_links


class TestExtraction(unittest.TestCase):
    
    def test_extract_markdown_images(self):
        text = "This is a ![link](url) to an image"
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0][0], "link")
        self.assertEqual(images[0][1], "url")
        
    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0][0], "to boot dev")
        self.assertEqual(links[1][1], "https://www.youtube.com/@bootdotdev")
        
    def test_extract_markdown_images_with_no_images(self):
        text = "This is text with no images"
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 0)
    
    def test_extract_markdown_links_with_no_links(self):
        text = "This is text with no links"
        links = extract_markdown_links(text)
        self.assertEqual(len(links), 0)
        
    def test_with_invalid_input(self):
        with self.assertRaises(TypeError, msg="Input must be a string"):
            extract_markdown_images(123)