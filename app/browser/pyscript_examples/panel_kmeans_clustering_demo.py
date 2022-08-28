from app.browser.html.html_helpers import script
from app.browser.widget.widget import Widget
from js import document, console
import js
from pyodide import create_proxy


class PanelKMeansClusteringDemoWidget(Widget):
    def __init__(self):
        super().__init__(  # language=HTML
            """
            <div>PanelKMeansClusteringDemoWidget</div>
              <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" type="text/css" />
    <link rel="stylesheet" href="https://unpkg.com/@holoviz/panel@0.13.1/dist/css/widgets.css" type="text/css" />
    <link rel="stylesheet" href="https://unpkg.com/@holoviz/panel@0.13.1/dist/css/markdown.css" type="text/css" />

    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/vega@5"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
    <script type="text/javascript" src="https://unpkg.com/tabulator-tables@4.9.3/dist/js/tabulator.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-2.4.2.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-2.4.2.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-2.4.2.min.js"></script>
    <script type="text/javascript" src="https://unpkg.com/@holoviz/panel@0.13.1/dist/panel.min.js"></script>
    <script type="text/javascript">
      console.log('it works!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
      Bokeh.set_log_level("info");
    </script>
        """)

    def after_render(self):
        self.container.id = "x-my-PanelKMeansClusteringDemoWidget"
        scripts = []
        for c in self.container.children:
            if c.tagName == 'SCRIPT':
                c.remove()
                scripts.append(c)
        scripts.reverse()

        def load_next(*args):
            console.log(f'load scripts len left:  {len(scripts)}')
            if len(scripts) == 0:
                console.log('load scripts done')
                return
            c = scripts.pop()
            console.log(f'script=`{c.innerHTML}`')
            s = script()
            s.type = s.type
            s.src = c.src
            js.eval(c.innerHTML)
            s.onload = create_proxy(load_next)
            document.body.append(s)

        load_next()
