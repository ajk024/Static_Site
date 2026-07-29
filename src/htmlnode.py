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
        if not self.props:
            return ""
        elif not isinstance(self.props, dict):
            raise TypeError("Incorrect 'props' type.")

        #parse props dictionary
        props_str: str = ""
        for key, val in self.props.items():
            if self.props[key] == None:
                continue
            props_str += f' {key}="{val}"'
        return props_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Leaf Node has no 'value' attribute.")
        elif not isinstance(self.value, str):
            raise TypeError("Value is not a string.")
        elif not self.tag:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"