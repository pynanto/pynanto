import os
import sys
import unittest
from pathlib import Path

from js import console


def unittest_main_fixed(module_name):
    module = sys.modules[module_name]
    test_suit = unittest.TestLoader().loadTestsFromModule(module)

    _test_runner_run(test_suit)


def run_all_tests():
    loader = unittest.TestLoader()
    browser = Path('./additional/app/browser').absolute()
    # (browser / '__init__.py').write_text('')
    test_suit = loader.discover(str(browser))
    _test_runner_run(test_suit)


def _test_runner_run(test_suit):
    txt = 'test_result.txt'
    with open(txt, 'w') as f:
        unittest.TextTestRunner(stream=f).run(test_suit)
    c = Path(txt).read_text()
    console.log(c)
