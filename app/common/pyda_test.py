import json
import unittest

from app.common.pyda import User, get_user


class MyTestCase(unittest.TestCase):
    def test_something(self):
        u = get_user()
        j = u.json()
        print('json str', j)
        r = User(**json.loads(j))
        print('obj restored', r)


if __name__ == '__main__':
    unittest.main()
