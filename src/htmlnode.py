from __future__ import annotations

class HTMLNode():
    def __init__(self, tag: str=None, 
                 value: str=None, 
                 children: list[HTMLNode]=None, 
                 props: dict[str]=None
                 ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == "" or self.props == None:
            return ""
        elif not isinstance(self.props, dict):
            raise TypeError("Incorrect 'props' type.")

        #parse props dictionary
        props_str: str = ""
        for key in self.props:
            props_str += f" {key}={self.props[key]}"
        return props_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props=None):
        super.__init__(self, tag, value, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf Node has no 'value' attribute.")
        elif not isinstance(self.value, str):
            raise TypeError("Value is not a string.")
        elif not self.tag:
            return self.value

        if self.tag == "p":
            return f"<p>{self.value}<\p>"
        elif self.tag == "a":
            return f"<a{self.props_to_html}>{self.value}<\a>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"