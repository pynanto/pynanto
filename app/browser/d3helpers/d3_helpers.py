from typing import Tuple, TypeVar
import d3

from app.browser.html.dom_definitions import HTMLElement
from app.common.app_geometry.size import Size

Td3SelectionSvg = TypeVar('Td3SelectionSvg')  # d3.Selection<SVGSVGElement, any, any, any>
Td3SelectionAny = TypeVar('Td3SelectionAny')  # d3.Selection<any, any, any, any>
Td3SelectionG = TypeVar('Td3SelectionG')  # d3.Selection<SVGGElement, any, any, any>


def removeDomainLine(g: Td3SelectionAny):
    g.select('.domain').remove()


def translate(left_top: Tuple[int, int]):
    left = left_top[0]
    top = left_top[1]
    return f'translate({left},{top})'


def newD3Svg(containerElement: HTMLElement, size: Size) -> Td3SelectionSvg:
    return (
        d3.select(containerElement)
        .append('svg')
        .attr('width', size.width)
        .attr('height', size.height)
    )


def newD3Group(root: Td3SelectionAny, translation: Tuple[int, int] = None):
    g = root.append("g")
    if translation is not None:
        g.attr('transform', translate(translation))
    return g
