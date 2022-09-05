import asyncio
from asyncio import Future

from app.browser.html.dom_definitions import HTMLElement
from app.browser.html.html_helpers import li
from app.browser.html.dom_async import load_script, run_async
from app.browser.widget.widget import Widget
from app.browser.widget_components.edit_widget import EditWidget
from app.common.api.api_product import ApiProductResponse, ApiProductRequest
from js import document, console, localStorage
from pyodide.ffi import create_proxy
import js


class FutureWidget(Widget):
    def __init__(self):
        super().__init__(  # language=HTML
            """
            <h2>FutureWidget</h2>
            <div id='ed1'></div>
            <button id="btn1">load js</button>
            """
        )
        self.ed1 = self(lambda: EditWidget('Js script url'))
        self.btn1 = self

    def after_render(self):
        self.btn1.onclick = create_proxy(self.btn_click)
        self.ed1.oninput = self._save_url
        item = localStorage.getItem('future-widget-url')
        if item is None or item == '':
            item = 'https://d3js.org/d3.v7.min.js'
        self.ed1.value = item

    def _save_url(self, *args):
        console.log('oninput!', self.ed1.value)
        localStorage.setItem('future-widget-url', self.ed1.value)

    def btn_click(self, *args):
        console.log('btn_click')

        async def doit():
            console.log('btn_click doit() start')
            await load_script(src=self.ed1.value)
            console.log('btn_click doit() end')

        run_async(doit())
        console.log('btn_click dopo run_async')
