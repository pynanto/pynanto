from typing import TypeVar, List


class HTMLElement:
    innerHTML: str
    innerText: str
    outerHTML: str
    tagName: str
    children: List['HTMLElement']

    def append(self, element: 'HTMLElement'):
        pass

    def remove(self):
        pass
