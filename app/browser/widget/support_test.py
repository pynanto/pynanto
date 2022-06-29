import unittest
from functools import partial
from typing import Callable, TypeVar, Type


class WidgetConstructor:
    pass


class MyTestCase(unittest.TestCase):
    def test_dynamic_cached_property(self):
        counter = 0

        class GuineaPig:
            def __init__(self):
                nonlocal counter
                counter += 1

        def lazy(fun: Callable[[], T]) -> T:
            p = WidgetConstructor(fun)
            return p

        class Target:
            def __init__(self):
                self.prop1 = lazy(lambda: GuineaPig())

            def __getattribute__(self, item):
                print(item)

            def __getattr__(self, item):
                print(item)

        target = Target()
        print(target.foo)
        self.assertEqual(0, counter)
        self.assertIsNotNone(target.prop1)
        self.assertEqual(1, counter)
        self.assertTrue(isinstance(target.prop1, GuineaPig))
        self.assertEqual(1, counter)

    def test_something(self):
        class WidSub(Wid):
            def __init__(self):
                super().__init__()
                self.wid = 'sub'

        class Wid1(Wid):

            def __init__(self):
                super().__init__()
                self.sub1 = self(lambda: WidSub())
                self.bind_self_elements()

        target = Wid1()


T = TypeVar('T')


class Wid:
    def __init__(self):
        pass

    def __call__(self, fun: Callable[[], T]) -> T:
        pass

    def bind_self_elements(self):
        for key, value in self.__dict__.items():
            if value != self:
                continue

            self.__dict__[key] = element

    def widget(self, fun: Callable[[], T]) -> T:
        pass


if __name__ == '__main__':
    unittest.main()
