from textnode import TextType
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from parentnode import ParentNode

def text_to_children(text):
    children = []
    for text_node in text_to_textnodes(text):
        children.append(text_node_to_html_node(text_node))
    return children

def markdown_to_html_node(markdown):
    result = []
    for block in markdown_to_blocks(markdown):
        if block_to_block_type(block) == BlockType.HEADING:
            level = block.split(" ")[0].count("#")
            tag = f"h{level}"

    return ParentNode(tag="div", result)

