import unittest

import rectangle


class RectangleTest(unittest.TestCase):
    def test_area_basic(self):
        res = rectangle.area(10, 2)
        self.assertEqual(res, 20)

    def test_area_zero(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = rectangle.area(1.23, 4.56)
        self.assertAlmostEqual(res, 5.6088)

    def test_perimeter_basic(self):
        res = rectangle.perimeter(10, 2)
        self.assertEqual(res, 24)

    def test_perimeter_zero(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)
