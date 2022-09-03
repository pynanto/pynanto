from app.browser.html.dom_definitions import HTMLElement
from app.browser.html.html_helpers import script
from app.browser.widget.widget import Widget
from js import document, console
import js
from pyodide.ffi import create_proxy


class PanelKMeansClusteringDemoWidget(Widget):
    def __init__(self):
        super().__init__(  # language=HTML
            """
            <div>PanelKMeansClusteringDemoWidget</div>
            <button id='_btn0' >load js libs</button>
            <button id='_btn1' >load python libs</button>
            <div class="container-fluid d-flex flex-column vh-100 overflow-hidden" id="container">
    <nav class="navbar navbar-expand-md navbar-dark sticky-top shadow" id="header" style="background-color: #000000;">
        <button type="button" class="navbar-toggle collapsed" id="sidebarCollapse">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="app-header">
            <a class="navbar-brand app-logo" href="/">
                <disabled-img src="./logo.png" class="app-logo">
            </a>
            <a class="title" href="" style="color: #f0ab3c;">Panel KMeans Clustering Demo</a>
        </div>
    </nav>

    <div class="row overflow-hidden" id="content">
        <div class="sidenav" id="sidebar">
            <ul class="nav flex-column">
                <div class="bk-root" id="x-widget"></div>
                <div class="bk-root" id="y-widget"></div>
                <div class="bk-root" id="n-widget"></div>
            </ul>
        </div>
        <div class="col mh-100 float-left" id="main">
            <div class="bk-root" id="intro"></div>
            <div class="bk-root" id="cluster-plot"></div>
            <div class="bk-root" id="table"></div>
        </div>
    </div>
</div>


    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://unpkg.com/@holoviz/panel@0.13.1/dist/bundled/bootstraptemplate/bootstrap.css">
    <link rel="stylesheet" href="https://unpkg.com/@holoviz/panel@0.13.1/dist/bundled/defaulttheme/default.css">

    <style>
        #sidebar {
            width: 350px;
        }
    </style>
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" type="text/css"/>
    <link rel="stylesheet" href="https://unpkg.com/@holoviz/panel@0.13.1/dist/css/widgets.css" type="text/css"/>
    <link rel="stylesheet" href="https://unpkg.com/@holoviz/panel@0.13.1/dist/css/markdown.css" type="text/css"/>


    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/vega@5"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/vega-lite@5"></script>
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
    <script type="text/javascript" src="https://unpkg.com/tabulator-tables@4.9.3/dist/js/tabulator.js"></script>

    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-2.4.2.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-widgets-2.4.2.min.js"></script>
    <script type="text/javascript" src="https://cdn.bokeh.org/bokeh/release/bokeh-tables-2.4.2.min.js"></script>

    <script type="text/javascript" src="https://unpkg.com/@holoviz/panel@0.13.1/dist/panel.min.js"></script>

  
    
        """)
        self._btn0: HTMLElement = self
        self._btn1: HTMLElement = self

    def after_render(self):
        self._btn1.disabled = True
        self.container.id = "x-my-PanelKMeansClusteringDemoWidget"

        self._btn0.onclick = create_proxy(self.btn0_click)
        self._btn1.onclick = create_proxy(self.btn1_click)

    async def btn0_click(self, *args):
        scripts = []
        console.log('listing scripts')
        elements = self.container.getElementsByTagName('script')
        console.log(f'len(elements)={len(elements)}')
        for c in elements:
            scripts.append(c)

        for c in scripts:
            c.remove()

        scripts.reverse()
        console.log('recap scripts')
        for c in scripts:
            console.log(f'   src=`{c.src}`')

        def load_next(*args):
            console.log(f'load scripts len left:  {len(scripts)}')
            if len(scripts) == 0:
                console.log('load scripts done')
                self._btn0.disabled = True
                self._btn1.disabled = False
                return
            c = scripts.pop()
            printableHtml = c.innerHTML.replace("\n", " ")
            console.log(f'load_next src=`{c.src}` script=`{printableHtml}`')
            s = script()
            s.type = s.type
            s.src = c.src
            if s.src == '':
                js.eval(c.innerHTML)
                console.log('loading next')
                load_next()
            else:
                s.onload = create_proxy(load_next)
                document.body.append(s)

        load_next()

    async def btn1_click(self, *args):
        self._btn1.disabled = True
        console.log('after_append()')
        import micropip
        await micropip.install(['altair', 'numpy', 'pandas', 'scikit-learn', 'panel==0.13.1'])
        import app.browser.pyscript_examples.panel_kmeans.pyscript_example as ex
        anti_removal = ex.url
