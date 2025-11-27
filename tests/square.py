import unittest

import square


class SquareTest(unittest.TestCase):
    def test_area_basic(self):
        res = square.area(3)
        self.assertAlmostEqual(res, 9.0)

    def test_area_zero(self):
        res = square.area(0)
        self.assertAlmostEqual(res, 0)

    def test_perimeter_basic(self):
        res = square.perimeter(3)
        self.assertAlmostEqual(res, 12)

    def test_perimeter_float(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
