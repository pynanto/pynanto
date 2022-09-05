from app.browser.d3helpers.d3_helpers import newD3Group
from app.browser.d3helpers.d3_load import load_d3
from app.browser.html.dom_async import run_async
from app.browser.html.dom_definitions import HTMLElement
from app.browser.keyboard.hotkey import Hotkey
from app.browser.widget.widget import Widget
from js import d3, console
from pyodide.ffi import create_proxy, to_js


class UseCase02_Widget(Widget):
    def __init__(self):
        super().__init__(  # language=HTML
            """
            <h2>UseCase02_Widget</h2>
            <svg id="root"></svg>
            <br>
            <label>prevent default <input type='checkbox' id='cb1'></label> 
            <br>
            <textarea id="taLog" style='font-size: 0.7em' cols='60' rows='15'></textarea>
            """
        )
        self.root = self
        self.cb1:HTMLElement = self
        self.taLog: HTMLElement = self

    def after_render(self):
        hk = Hotkey(self.container)
        # hk.enable_log = True
        hk.add('CTRL-ALT-R', self._hotkey_callback)
        hk.add('E', self._hotkey_callback2)
        run_async(self.after_render_async2())

    def _hotkey_callback(self, event):
        self.taLog.value += 'CTRL-ALT-R pressed!\n'

    def _hotkey_callback2(self, event):
        msg = 'prevent default' if self.cb1.checked else 'let it flow'
        self.taLog.value += f'E pressed! {msg}\n'
        return self.cb1.checked

    async def after_render_async2(self):
        gBrush = newD3Group(d3.select(self.root))
        brush = d3.brushX().on("end", create_proxy(self.on_brush_end))
        brush.extent(to_js([[0, 0], [400, 100]]))
        gBrush \
            .call(brush) \
            .call(brush.move, to_js([40, 70])) \
            .lower()

    def on_brush_end(self, event, *args):
        console.log('on_brush_end', event)
        selection = event.selection
        console.log('on_brush_end selection', selection)
        self.taLog.value += f'on_brush_end selection {selection}\n'
        start = selection[0]
        end = selection[1]
        console.log(start + 1, end + 2)
