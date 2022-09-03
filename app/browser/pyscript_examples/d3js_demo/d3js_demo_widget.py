from app.browser.widget.widget import Widget


class D3_DemoWidget(Widget):
    def __init__(self):
        super().__init__(  # language=HTML
            """
         <div>
          <div style="text-align: center">PyScript version</div>
          <div id="py">
            <div class="loading"></div>
          </div>
        </div>
        """
        )

    def after_render(self):
        import app.browser.d3play.app_d3 as ex
        anti_removal = ex.__name__
