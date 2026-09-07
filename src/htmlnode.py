from types import NoneType

from numpy import isin

from textnode import TextNode


class HTMLNode:
    def __init__(self, tag: str | None = None,
                 value: str | None = None,
                 children: list[HTMLNode] | None = None,
                 props: dict[TextNode] | None = None):
        self.tag: str | None = tag
        self.value: str | None = value
        self.children: list[HTMLNode] | None = children
        self.props: dict[TextNode] | None = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result: str = ""

        for key, value in self.props.items():
            result += f' {key}="{value}"'

        return result.strip()

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props_to_html()})"

    def to_html(self):
        if self.value == None:
            raise ValueError

        if self.tag == None:
            return self.value

        if self.props != None:
            return f"<{self.tag} {self.props.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError

        if self.children == None:
            return ValueError

        children_html = "".join(child.to_html() for child in self.children)

        props_str = f" {self.props_to_html()}" if self.props else ""

        return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"