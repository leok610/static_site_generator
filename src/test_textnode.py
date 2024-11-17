import unittest

from textnode import NodeType, TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", NodeType.BOLD)
        node2 = TextNode("This is a text node", NodeType.BOLD)
        self.assertEqual(node, node2)
    def test_italic(self):
        node = TextNode("Herro", NodeType.ITALIC, "scoobydoo.de")
        node2 = TextNode("Herro", NodeType.ITALIC, "scoobydoo.de")
        self.assertEqual(node, node2)
    def test_code(self):
        node = TextNode("Herro", NodeType.CODE, "scoobydoo.de")
        node2 = TextNode("Herro", NodeType.CODE, "scoobydoo.de")
        self.assertEqual(node, node2)
    def test_links(self):
        node = TextNode("Herro", NodeType.LINKS, "scoobydoo.de")
        node2 = TextNode("Herro", NodeType.LINKS, "scoobydoo.de")
        self.assertEqual(node, node2)
    def test_images(self):
        node = TextNode("Herro", NodeType.IMAGES, "scoobydoo.de")
        node2 = TextNode("Herro", NodeType.IMAGES, "scoobydoo.de")
        self.assertEqual(node, node2)
    def test_diff(self):
        node = TextNode("Herro", NodeType.LINKS, "scoobydoo.de")
        node2 = TextNode("Herro", NodeType.CODE, "scoobydoo.de")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
