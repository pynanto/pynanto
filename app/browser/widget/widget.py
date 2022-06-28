from js import document, window, console, setInterval, fetch
import abc


class Widget:
    def __init__(self, html: str):
        self.html = html
        self.div = document.createElement('div')
        self.div.innerHTML = html
        self.after_render()

    def append_to(self, container_element):
        container_element.append(self.div)
        return self

    def after_render(self):
        pass

    def bind_self_elements(self):
        for key, value in self.__dict__.items():
            if value != self:
                continue
            console.log('found you!', key)
            element = self.div.querySelector('#' + key)
            if element is None:
                raise Exception(f'Element not found, name:[{key}] html: [{self.html}]')
            self.__dict__[key] = element
