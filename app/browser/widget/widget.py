from functools import cache
from typing import TypeVar, Callable

from js import document, window, console, setInterval, fetch
import abc

from app.browser.html.dom_definitions import HTMLElement

T = TypeVar('T')


class WidgetConstructor:
    def __init__(self, constructor):
        self.constructor = constructor


class Widget:
    def __init__(self, html: str):
        self.html = html
        self._expanded = False
        self._container: HTMLElement = None

    def __call__(self, fun: Callable[[], T]) -> T:
        return WidgetConstructor(fun)

    @property
    def container(self):
        if self._container is None:
            self._container = document.createElement('div')

        if not self._expanded:
            self._expanded = True
            self._container.innerHTML = self.html
            self.bind_self_elements()
            self.after_render()

        return self._container

    def append_to(self, container_element):
        container_element.append(self.container)
        return self

    def after_render(self):
        pass

    def bind_self_elements(self):
        def get_binder(value):
            if value == self:
                return lambda element: element
            if isinstance(value, WidgetConstructor):
                def wc_binder(element):
                    instance: Widget = value.constructor()
                    instance._container = element
                    return instance

                return wc_binder
            return None

        for key, value in self.__dict__.items():
            binder = get_binder(value)
            if binder is None:
                continue

            element = self.container.querySelector('#' + key)
            if element is None:
                raise Exception(f'Element not found, name:[{key}] html: [{self.html}]')
            instance = binder(element)
            self.__dict__[key] = instance
