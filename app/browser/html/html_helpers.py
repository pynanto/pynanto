from functools import partial

from js import document, window, console, setInterval, fetch


def _ce(tag, html=None):
    element = document.createElement(tag)
    if html is not None:
        element.innerHTML = html
    return element


def div(): return _ce('div')


def button(): return _ce('button')


def br(): return _ce('br')


def ol(): return _ce('ol')


li = partial(_ce, 'li')
