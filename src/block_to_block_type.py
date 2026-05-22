from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def is_ordered_list(block):
    for i, line in enumerate(block.splitlines(), 1):
        if not line.startswith(f"{i}. "):
            return False
    return True

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in block.splitlines()):
        return BlockType.QUOTE
    elif all(line.startswith("- ") for line in block.splitlines()):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(block): 
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
