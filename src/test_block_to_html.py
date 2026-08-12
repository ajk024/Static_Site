import unittest
from functions import markdown_to_html_node

class TestBlockToHTML(unittest.TestCase):
    def test_28(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
        )

    def test_29(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_30(self):
        md = """- Item 1
- Item 2
- Item 3
- Item 4
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>- Item 1<li>\n<li>- Item 2<li>\n<li>- Item 3<li>\n<li>- Item 4<li></ul></div>"
        )

    def test_31(self):
        md = """1. Item 1
2. Item 2
3. Item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>1. Item 1<li>\n<li>2. Item 2<li>\n<li>3. Item 3<li></ol></div>"
        )

    def test_32(self):
        md = "### Heading 3"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>### Heading 3</h3></div>"
        )