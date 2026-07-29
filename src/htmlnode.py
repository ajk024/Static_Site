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