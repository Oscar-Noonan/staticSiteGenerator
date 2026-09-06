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