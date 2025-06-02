class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
 
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return "" 

        html = []
        props = self.props.items()
        for key, value in props:
            props_html = f'{key}="{value}"'
            html.append(props_html)
        return " " + " ".join(html)