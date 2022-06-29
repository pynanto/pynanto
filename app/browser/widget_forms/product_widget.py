from app.browser.widget.widget import Widget
from app.browser.widget_components.edit_widget import EditWidget
from app.common.api.api_product import ApiProductResponse, ApiProductRequest
from js import document, console

class ProductWidget(Widget):
    def __init__(self):
        super().__init__(# language=HTML
            """
            <h2>ProductWidget</h2>
            <div id='ed1'></div>
            <div id='ed2'></div>
            <div id='ed3'></div>
            """
        )
        self.ed1 = self(lambda: EditWidget('A'))
        self.ed2 = self(lambda: EditWidget('B'))
        self.ed3 = self(lambda: EditWidget('A*B'))

    def after_render(self):
        console.log('after render')
        ed1 = self.ed1
        ed2 = self.ed2

        async def run_sum():
            res: ApiProductResponse = await ApiProductRequest(a=ed1.value, b=ed2.value).send()
            self.ed3.value = str(res.product)

        for ed in [ed1, ed2]:
            ed.oninput = lambda x: run_sum()


