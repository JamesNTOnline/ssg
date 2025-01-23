import unittest 
import test_setup 
from markdown_extraction import extract_markdown_images, extract_markdown_links, markdown_to_blocks


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
            
    def test_markdown_to_blocks(self):
        markdown = "This is a markdown document\n\nwith multiple blocks\n\nand some extra text"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(blocks[0], "This is a markdown document")
        self.assertEqual(blocks[1], "with multiple blocks")
        self.assertEqual(blocks[2], "and some extra text")
    
    def test_markdown_to_blocks_with_spaces(self):
        markdown = "# Heading\n\n Paragraph 1\n \n\n * List item 1\nList item 2\n\n   \n \nParagraph 2"
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 4)   
        self.assertEqual(blocks[0], "# Heading")
        self.assertEqual(blocks[1], "Paragraph 1")
        self.assertEqual(blocks[2], "* List item 1\nList item 2")
        self.assertEqual(blocks[3], "Paragraph 2")
        
    def test_markdown_to_blocks_with_weird_spacing(self):
        markdown = "# Heading\n\n\n Paragraph with\nmultiple lines\n    and weird spacing\n\n* List start\n  * Indented list\n* List end\n  \n\n      \nLast paragraph\n         "
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(len(blocks), 4)
        self.assertEqual(blocks[0], "# Heading")
        self.assertEqual(blocks[1], "Paragraph with\nmultiple lines\n    and weird spacing")
        self.assertEqual(blocks[2], "* List start\n  * Indented list\n* List end")
        self.assertEqual(blocks[3], "Last paragraph")
        
        