import unittest
from functions import extract_markdown_images


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images_1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        node = extract_markdown_images(text)
        answer = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(node, answer)

if __name__ == "__main__":
    unittest.main()

