import unittest
from block_to_block_type import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_code(self):
        block = "```This is code```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_quote(self):
        block = """> This
> is
> a
> quote."""
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_unordered_list(self):
        block = """- This
- is
- a
- unordered
- list."""
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_valid_ordered_list(self):
        block1 = """1. This
2. is
3. an
4. ordered
5. list"""
        self.assertEqual(block_to_block_type(block1), BlockType.ORDERED_LIST)

    def test_invalid_ordered_list(self):
        block1 = """1. This
2. is
3. an
G. ordered
5. list"""
        self.assertEqual(block_to_block_type(block1), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()
