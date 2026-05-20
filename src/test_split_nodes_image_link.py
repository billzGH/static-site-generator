# src/test_split_nodes_image_link.py
import unittest
from textnode import TextNode, TextType
from split_nodes_image_link import split_nodes_image, split_nodes_link


class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual([
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
        ], new_nodes)

    def test_no_images(self):
        node = TextNode("just text", TextType.TEXT)
        self.assertListEqual([node], split_nodes_image([node]))

    def test_non_text_node_passed_through(self):
        node = TextNode("bold", TextType.BOLD)
        self.assertListEqual([node], split_nodes_image([node]))

    def test_image_at_start(self):
        node = TextNode("![img](https://url.com) then text", TextType.TEXT)
        result = split_nodes_image([node])
        self.assertEqual(result[0], TextNode("img", TextType.IMAGE, "https://url.com"))
        self.assertEqual(result[1], TextNode(" then text", TextType.TEXT))


class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual([
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ], new_nodes)

    def test_no_links(self):
        node = TextNode("just text", TextType.TEXT)
        self.assertListEqual([node], split_nodes_link([node]))

    def test_link_at_end(self):
        node = TextNode("click [here](https://boot.dev)", TextType.TEXT)
        result = split_nodes_link([node])
        self.assertEqual(result[0], TextNode("click ", TextType.TEXT))
        self.assertEqual(result[1], TextNode("here", TextType.LINK, "https://boot.dev"))


if __name__ == "__main__":
    unittest.main()
