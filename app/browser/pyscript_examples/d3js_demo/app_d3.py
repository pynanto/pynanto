from pyodide.ffi import create_proxy, to_js
# import d3

from js import document, console, d3

console.log('d3 version', d3.version)
if len(d3.version) < 3:
    raise Exception('d3 is not properly loaded')
from app.browser.d3helpers.d3_helpers import newD3Group

fruits = [
    dict(name="🍊", count=21),
    dict(name="🍇", count=13),
    dict(name="🍏", count=8),
    dict(name="🍌", count=5),
    dict(name="🍐", count=3),
    dict(name="🍋", count=2),
    dict(name="🍎", count=1),
    dict(name="🍉", count=1),
]

fn = create_proxy(lambda d, *_: d["count"])
data = d3.pie().value(fn)(to_js(fruits))

arc = (d3.arc()
       .innerRadius(210)
       .outerRadius(310)
       .padRadius(300)
       .padAngle(2 / 300)
       .cornerRadius(8))

div = document.createElement('div')
div.id = 'py'
document.body.append(div)
py = d3.select("#py")
py.select(".loading").remove()

svgorig = (py
           .append("svg")
           .attr("viewBox", "-320 -320 640 640")
           .attr("width", "400")
           .attr("height", "400"))

svg = newD3Group(svgorig, (0, 0))

for d in data:
    d_py = d.to_py()

    (svg.append("path")
     .style("fill", "steelblue")
     .attr("d", arc(d)))

    text = (svg.append("text")
            .style("fill", "white")
            .attr("transform", f"translate({arc.centroid(d).join(',')})")
            .attr("text-anchor", "middle"))

    (text.append("tspan")
     .style("font-size", "24")
     .attr("x", "0")
     .text(d_py["data"]["name"]))

    (text.append("tspan")
     .style("font-size", "18")
     .attr("x", "0")
     .attr("dy", "1.3em")
     .text(d_py["value"]))

console.log('*' * 20 + ' done')
