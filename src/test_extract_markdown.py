# src/test_extract_markdown.py
import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        text = "![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        self.assertListEqual([
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ], matches)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_multiple_links(self):
        text = "[boot dev](https://www.boot.dev) and [youtube](https://www.youtube.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual([
            ("boot dev", "https://www.boot.dev"),
            ("youtube", "https://www.youtube.com")
        ], matches)

    def test_links_does_not_match_images(self):
        text = "![image](https://img.url) [link](https://link.url)"
        matches = extract_markdown_links(text)
        self.assertListEqual([("link", "https://link.url")], matches)

    def test_no_matches(self):
        self.assertListEqual([], extract_markdown_images("no images here"))
        self.assertListEqual([], extract_markdown_links("no links here"))


if __name__ == "__main__":
    unittest.main()
