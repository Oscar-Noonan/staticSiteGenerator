import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is different text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.LINK, "www.boot.dev")
        node_as_string: str = repr(node)
        self.assertEqual(node_as_string, "TextNode(This is a text node, link, www.boot.dev)")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "www.boot.dev")
        self.assertEqual(node.url, "www.boot.dev")

    def test_link_none(self):
        node = TextNode("This is a text node", TextType.LINK, "www.boot.dev")
        self.assertNotEqual(node.url, None)

    def test_not_link(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_convert_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")


if __name__ == "__main__":
    unittest.main()