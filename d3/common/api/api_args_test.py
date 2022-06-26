import json
import unittest
from datetime import datetime

from d3.common.api.api_args import ApiSelectionRequest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        i = ApiSelectionRequest()
        print(i.json())
        i.window = [datetime.now(), datetime.now()]
        # i.window = [datetime.now()]
        print(i.json())

        r = ApiSelectionRequest(**json.loads(i.json()))


if __name__ == '__main__':
    unittest.main()
