import unittest

from app.browser.html.dom_definitions import HTMLElement
from app.browser.unittest import unittest_main_fixed
from app.browser.widget.widget import Widget


class WidgetTestCase(unittest.TestCase):
    def test_basic_bind(self):
        class Widget1(Widget):
            def __init__(self):
                super().__init__("<span id='span1'>foo</span>")
                self.span1: HTMLElement = self
                self.bind_self_elements()

        target = Widget1()
        self.assertEqual('foo', target.span1.innerHTML)

    def test_bad(self):
        pass


def main():
    unittest_main_fixed(__name__)


if __name__ == '__main__':
    main()
