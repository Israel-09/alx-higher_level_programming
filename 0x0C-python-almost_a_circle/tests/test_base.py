import unittest
from models.base import Base

class testBase(unittest.TestCase):

    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base(23)
        self.assertEqual(b2.id, 23)

if __name__ == '__main__':
    unittest.main()
