from app.browser.html.dom_definitions import HTMLElement
from app.browser.html.html_helpers import li
from app.browser.widget.widget import Widget
from app.browser.widget_components.edit_widget import EditWidget
from app.common.api.api_product import ApiProductResponse, ApiProductRequest
from js import document, console

from app.common.api.api_square import ApiSquareRequest, ApiSquareResponse


class SquareWidget(Widget):
    def __init__(self):
        super().__init__(  # language=HTML
            """
            <h2>SquareWidget</h2>
            <div id='ed1'></div>
            <div id='ed2'></div>
            """
        )
        self.ed1 = self(lambda: EditWidget('A'))
        self.ed2 = self(lambda: EditWidget('A*A'))

    def after_render(self):
        ed1 = self.ed1
        ed2 = self.ed2

        async def run_square():
            res: ApiSquareResponse = await ApiSquareRequest(x=ed1.value).send()
            ed2.value = str(res.square)

        ed1.oninput = lambda x: run_square()
