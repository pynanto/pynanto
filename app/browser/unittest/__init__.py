import sys
import unittest
from pathlib import Path

from js import console


def unittest_main_fixed(module_name):
    txt = 'test_result.txt'

    with open(txt, 'w') as f:
        module = sys.modules[module_name]
        suite = unittest.TestLoader().loadTestsFromModule(module)
        unittest.TextTestRunner(stream=f).run(suite)

    c = Path(txt).read_text()
    console.log(c)
