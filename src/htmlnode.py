class HTMLNode:
    def __init__(self, tag, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        ):
            return True
        return False

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_str = ""
        if not self.props:
            return props_str
        for prop in self.props:
            props_str += f' {prop}="{self.props[prop]}"'
        return props_str

    def __repr__(self) -> str:
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError(f"{self.tag} must have a value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode(tag: {self.tag}, value: {self.value}, props: {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError(f"{self.tag} must have a tag")
        if self.children is None:
            raise ValueError(f"{self.tag} must have children")

        def child_chain(children, result=""):
            if len(children) <= 0:
                return result
            child = children[0]
            result += child.to_html()
            return child_chain(children[1:], result)

        children = child_chain(self.children, "")

        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"
