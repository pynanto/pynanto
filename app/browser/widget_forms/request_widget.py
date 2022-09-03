import json

from app.browser.html.dom_definitions import HTMLElement
from app.browser.html.html_helpers import li
from app.browser.widget.widget import Widget
from app.browser.widget_components.edit_widget import EditWidget
from app.common.api.api_product import ApiProductResponse, ApiProductRequest
from js import document, console, fetch
import js

from app.common.api.api_square import ApiSquareRequest, ApiSquareResponse


class RequestWidget(Widget):
    def __init__(self):
        super().__init__(  # language=HTML
            """<h2>RequestWidget</h2>

<div style="display: flex">
    <div id='ed1'></div>
    <button id="btn_get" >Issue request GET</button>
</div>
<br>
<div>
    <label>Body</label>
    <br>
    <textarea id='ed2' style='font-size: 0.7em' cols='30' rows='3'></textarea>
    <br>
    <button id="btn_post">Issue request POST</button>   
</div>
<br>
<textarea id="taLog" style='font-size: 0.7em' cols='120' rows='40'></textarea>
<button id="btn_pretty">JSON prettify</button>
<br>
"""
        )
        self.ed1 = self(lambda: EditWidget('Url'))
        self.ed2 = self
        self.taLog = self

    def after_render(self):
        self._fields_load()

    async def btn_get__click(self, *args):
        await self.execute_fetch(
            self.ed1.value,
            method='GET'
        )

    async def btn_post__click(self, *args):
        await self.execute_fetch(
            self.ed1.value,
            method='POST',
            body=self.ed2.value
        )

    async def execute_fetch(self, *args, **kwargs):
        self._fields_save()
        try:
            response = await fetch(*args, **kwargs)
            text = await response.text()
            self.taLog.value = text
        except Exception as ex:
            self.taLog.value     = str(ex)

        self._fields_save()

    def _fields_load(self):
        self.ed1.value = js.localStorage.getItem('request_widget.ed1')
        self.ed2.value = js.localStorage.getItem('request_widget.ed2')
        self.taLog.value = js.localStorage.getItem('request_widget.taLog')

    def _fields_save(self):
        js.localStorage.setItem('request_widget.ed1', self.ed1.value)
        js.localStorage.setItem('request_widget.ed2', self.ed2.value)
        js.localStorage.setItem('request_widget.taLog', self.taLog.value)

    def btn_pretty__click(self, *args):
        parsed = json.loads(self.taLog.value)
        pretty = json.dumps(parsed, indent=4)
        self.taLog.value = pretty
        self._fields_save()
