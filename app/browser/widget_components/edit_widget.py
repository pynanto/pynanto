# from app.browser import Widget
from app.browser.html.dom_definitions import HTMLElement
from app.browser.widget.widget import Widget
from pyodide import create_proxy, to_js
from js import console


def element(f):
    print(f)


class EditWidget(Widget):

    def __init__(self, title: str = ''):
        super().__init__(  # language=HTML
            """
            <span id="_title"></span>
            <input id="_input1">
            <br>
            """
        )
        self.title = title
        self._input1: HTMLElement = self
        self._title: HTMLElement = self

    def after_render(self):
        self._title.innerHTML = self.title
        self.oninput = lambda e: None
        self._input1.oninput = create_proxy(lambda e: self.oninput(e))

    @property
    def value(self) -> str:
        return self._input1.value

    @value.setter
    def value(self, val: str):
        self._input1.value = val
