import json
from itertools import groupby
from pathlib import Path
from typing import Dict

from app.browser.d3helpers.d3_helpers import newD3Group
from app.browser.d3helpers.d3_load import load_d3
from app.browser.html.dom_async import run_async
from app.browser.html.dom_definitions import HTMLElement
from app.browser.keyboard.hotkey import Hotkey
from app.browser.widget.widget import Widget
from js import d3, console
from pyodide.ffi import create_proxy, to_js

from app.common.itertools import associateby
from app.common.time import time_wrapper
from app.common.use_case_01.datachart_args import ApiDatachartCsvDataResponse, ApiDatachartCsvInfoResponse, \
    ColumnValues, ValueColumn


class UseCase02a_Widget(Widget):
    def __init__(self):
        super().__init__(  # language=HTML
            """
            <h2>UseCase02a_Widget x</h2>
            <svg id="root"></svg>
            <br>
            <br>
            <textarea id="taLog" style='font-size: 0.7em' cols='60' rows='15'></textarea>
            """
        )
        self.root = self
        self.taLog: HTMLElement = self

    def after_render(self):
        self.taLog.value += f'UseCase02a_Widget\n'
        self.after_render_async2()

    @time_wrapper()
    def after_render_async2(self):
        data: ApiDatachartCsvDataResponse = json_to_instance(ApiDatachartCsvDataResponse, 'data.json')
        data_dict = associateby(data.column_values, lambda c: c.name)
        info: ApiDatachartCsvInfoResponse = json_to_instance(ApiDatachartCsvInfoResponse, 'info.json')
        columns: Dict[str, ValueColumn] = {}
        for col in info.columns:
            vals: ColumnValues = data_dict.get(col.name, None)
            if vals is not None:
                colval = ValueColumn(values=vals.values, **vars(col))
                columns[col.name] = colval
                console.log('='*30 + col.name)


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


def json_to_instance(response, data_json):
    text = (Path(__file__).parent / data_json).read_text()
    args = json.loads(text)
    resp = response(**args)
    return resp
