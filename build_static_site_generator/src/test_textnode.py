import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node, node2)

    def test_eq_empty(self):
        node = TextNode("", TextType.ITALIC, "http://bootdev.com")
        node2 = TextNode("", TextType.ITALIC, "http://bootdev.com")
        self.assertEqual(node, node2)
    def test_eq_None_set(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_texttype_diff(self):
        node = TextNode("This is a text node", TextType.ITALIC, "http://example.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://example.com")
        self.assertNotEqual(node, node2)

    def test_eq_extra_spaces(self):
        node = TextNode("This is a text node", TextType.ITALIC, "http://bootdev.com")
        node2 = TextNode("This is a text node   ", TextType.ITALIC, "http://bootdev.com")
        self.assertNotEqual(node, node2)


    


if __name__ == "__main__":
    unittest.main()


