import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_repr(self):
        node = LeafNode("p", "This is some example text", {"href": "https://www.google.com",})
        node_as_string: str = repr(node)
        self.assertEqual(node_as_string, 'LeafNode(p, This is some example text, href="https://www.google.com")')
            
    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")


if __name__ == "__main__":
    unittest.main()