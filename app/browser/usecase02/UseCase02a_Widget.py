import json
from datetime import datetime
from itertools import groupby
from pathlib import Path
from types import SimpleNamespace
from typing import Dict, List, Iterable

from pydantic import BaseModel

from app.browser.d3helpers.d3_helpers import newD3Group
from app.browser.d3helpers.d3_load import load_d3
from app.browser.html.dom_async import run_async
from app.browser.html.dom_definitions import HTMLElement
from app.browser.keyboard.hotkey import Hotkey
from app.browser.widget.widget import Widget
from js import d3, console, Date
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
            <svg id="root" style="width: 2000px; height: 400px"></svg>
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
        gBrush = newD3Group(d3.select(self.root))
        gContent = gBrush

        data: ApiDatachartCsvDataResponse = json_to_instance(ApiDatachartCsvDataResponse, 'data-2041.json')
        data_dict = associateby(data.column_values, lambda c: c.name)
        info: ApiDatachartCsvInfoResponse = json_to_instance(ApiDatachartCsvInfoResponse, 'info.json')
        columns: Dict[str, ValueColumn] = {}
        for col in info.columns:
            vals: ColumnValues = data_dict.get(col.name, None)
            if vals is not None:
                colval = ValueColumn(values=vals.values, **vars(col))
                columns[col.name] = colval
                # console.log('=' * 30 + col.name)
                ColumnPlot(gContent, colval, data.timestamp_values, []).render()

        # brush = d3.brushX().on("end", create_proxy(self.on_brush_end))
        # brush.extent(to_js([[0, 0], [400, 100]]))
        # gBrush \
        #     .call(brush) \
        #     .call(brush.move, to_js([40, 70])) \
        #     .lower()

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


def filter_out_none(x: List[datetime], y: List[object]):
    return zip(*((x1, y1) for x1, y1 in zip(x, y) if y1 is not None))


def datetime_to_jsdate(d: datetime) -> Date:
    return Date.new(d.isoformat())


def to_js_datetime(iterable: Iterable[datetime]) -> List[Date]:
    return list(map(datetime_to_jsdate, iterable))


class ColumnPlot:
    def __init__(
            self,
            gContent,
            column: ValueColumn,
            x_all_values: List[datetime],
            label_columns: List[ValueColumn]
    ):
        self.gContent = gContent
        self.column = column
        self.x_all_values = x_all_values
        self.label_columns = label_columns
        self.x_values, self.y_values = filter_out_none(x_all_values, column.values)

    def render(self):
        geo = SimpleNamespace()
        geo.y_range = [400, 0]
        geo.x_range = [0, 600]
        y_scale = d3.scaleLinear() \
            .domain(d3.extent(to_js(self.y_values))) \
            .range(to_js(geo.y_range))

        x_scale = d3.scaleTime() \
            .domain(d3.extent(to_js_datetime(self.x_all_values))) \
            .range(to_js(geo.x_range))

        def x_mapper(tup, *args):
            # console.log('tup', str(tup), 'args', str(args))
            x: datetime
            index, x = tup
            y = self.y_values[index]
            # console.log('index', index, 'x', x, 'y', y)
            point = Point(
                x=x,
                y=y,
                x_scaled=x_scale(datetime_to_jsdate(x)),
                y_scaled=y_scale(y),
            )
            return point

        points: List[Point] = list(map(x_mapper, enumerate(self.x_values)))
        d: Point
        self.gContent \
            .append('g') \
            .selectAll('myCircles') \
            .data(to_js(points)) \
            .enter() \
            .append("circle") \
            .attr("fill", lambda d, *args: self.column.color) \
            .attr("stroke", "none") \
            .attr("cx", lambda d, *args: d.x_scaled) \
            .attr("cy", lambda d, *args: d.y_scaled) \
            .attr("r", 3) \
            .attr('fill-opacity', 0.7)

        # self.gContent \
        #     .append('g') \
        #     .append('path') \
        #     .datum(to_js(data)) \
        #     attr()


class Point(BaseModel):
    x: datetime
    y: float

    x_scaled: int
    y_scaled: int

    # color: str
