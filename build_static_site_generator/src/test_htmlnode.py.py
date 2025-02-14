import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("b")
        result = ""
        self.assertEqual(node.props_to_html(), result)
    
 
    
        



    


if __name__ == "__main__":
    unittest.main()


