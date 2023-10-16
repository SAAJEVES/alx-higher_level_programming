#!/usr/bin/python3

"""Running Unittest on Base Class"""

import unittest
from models import base


class TestBase(unittest.TestCase):
    """Creating A Unittest case for Base Class"""

    def setUp(self):
        self.b1 = base.Base()
        self.b2 = base.Base()
        self.b3 = base.Base()
        self.b4 = base.Base(12)
        self.b5 = base.Base()

    def test_id(self):
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


if __name__ == "__main__":
    unittest.main()
