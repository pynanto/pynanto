from typing import TypeVar, List


class Event:
    pass


class EventTarget:
    def addEventListener(self, type: str, callback, options=None):
        pass

    def dispatchEvent(self, event: Event) -> bool:
        pass

    def removeEventListener(self, type: str, callback, options=None):
        pass


class HTMLElement(EventTarget):
    innerHTML: str
    innerText: str
    outerHTML: str
    tagName: str
    children: List['HTMLElement']

    def append(self, element: 'HTMLElement'):
        pass

    def remove(self):
        pass
