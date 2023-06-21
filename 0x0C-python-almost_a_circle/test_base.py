import unittest
from models import base


class testBase(unittest.TestCase):

    def test_id(self):
        b1 = base.Base()
        self.assertEqual(b1.id, 1)

if __name__ == '__main__':
    unittest.main()
