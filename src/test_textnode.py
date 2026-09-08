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

    def test_convert_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_convert_italic(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is a italic node")

    def test_convert_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_convert_link(self):
        node = TextNode("This is a link node", TextType.LINK, "boot.dev")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props, {"href": "boot.dev"})

    def test_convert_image(self):
        node = TextNode("This is a image node", TextType.IMAGE, "boots.png")
        html_node = node.text_node_to_html_node()
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, None)
        self.assertEqual(html_node.props, {"src": "boots.png", "alt": "This is a image node"})


if __name__ == "__main__":
    unittest.main()