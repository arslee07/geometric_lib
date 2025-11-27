import math
import unittest

import circle


class CircleTest(unittest.TestCase):
    def test_area_basic(self):
        res = circle.area(3)
        self.assertAlmostEqual(res, math.pi * 9.0)

    def test_area_zero(self):
        res = circle.area(0)
        self.assertAlmostEqual(res, 0)

    def test_perimeter_basic(self):
        res = circle.perimeter(3)
        self.assertAlmostEqual(res, math.pi * 6.0)

    def test_perimeter_float(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
