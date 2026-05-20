# src/test_markdown_to_blocks.py
import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "This is **bolded** paragraph",
            "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
            "- This is a list\n- with items",
        ])

    def test_extra_newlines(self):
        md = "block one\n\n\n\nblock two"
        self.assertEqual(markdown_to_blocks(md), ["block one", "block two"])

    def test_strips_whitespace(self):
        md = "  block one  \n\n  block two  "
        self.assertEqual(markdown_to_blocks(md), ["block one", "block two"])

    def test_single_block(self):
        md = "just one block"
        self.assertEqual(markdown_to_blocks(md), ["just one block"])


if __name__ == "__main__":
    unittest.main()
