from html.parser import HTMLParser
from task4 import Stack


class TagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = Stack()
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag in ("br", "img", "meta", "link", "input", "hr"):
            return
        self.stack.push(tag)

    def handle_endtag(self, tag):
        if self.stack.is_empty():
            self.errors.append(f"лишний закрывающий тег </{tag}>")
            return
        top = self.stack.pop()
        if top != tag:
            self.errors.append(f"ожидался </{top}>, получен </{tag}>")


def check_html(text):
    parser = TagChecker()
    parser.feed(text)
    while not parser.stack.is_empty():
        parser.errors.append(f"не закрыт тег <{parser.stack.pop()}>")
    return parser.errors


def run_tests():
    good = "<html><head><title>Example</title></head><body><h1>Hello</h1></body></html>"
    print("Корректный:", check_html(good))

    bad1 = "<html><body><h1>Hello</body></html>"
    print("Несовпадение:", check_html(bad1))

    bad2 = "<html><body><h1>Hello</h1></body>"
    print("Не закрыт html:", check_html(bad2))

    bad3 = "<html></body></html>"
    print("Лишний </body>:", check_html(bad3))


if __name__ == "__main__":
    run_tests()