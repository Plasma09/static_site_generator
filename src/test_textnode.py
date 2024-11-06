import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    #Testing equality with 2 identic nodes
    def test_eq_one(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    #Testing equality with the first text changed
    def test_eq_two(self):
        node = TextNode("This is in fact not a test node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    #Testing equality with the second text type changed
    def test_eq_three(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    #Testing equality with only the first url added
    def test_eq_four(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.testnode.com")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    #Testing equality with 2 urls added but an extra space in the second text
    def test_eq_five(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://www.testnode.com")
        node2 = TextNode("This is a text node ", TextType.BOLD, "http://www.testnode.com")
        self.assertNotEqual(node, node2)

    #Testing equality with 2 urls added
    def test_eq_six(self):
        node = TextNode("This is a text node", TextType.ITALIC, "http://www.testnode.com")
        node2 = TextNode("This is a text node", TextType.ITALIC, "http://www.testnode.com")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
