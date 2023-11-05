import unittest

def area(a):
    return a * a


def perimeter(a):
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_positive_integer_side_area(self):
        res = area(2)
        self.assertEqual(res, 4)
    def test_negative_integer_sides_area(self):
        res = area(-2)
        self.assertEqual(res, "IllegalArgumentException")

    def test_positive_integer_side_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 8)
    def test_negative_integer_side_perimeter(self):
        res = perimeter(-2)
        self.assertEqual(res, "IllegalArgumentException")

    def test_positive_float_side_area(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)
    def test_negative_float_side_area(self):
        res = area(-2.5)
        self.assertEqual(res, "IllegalArgumentException")

    def test_positive_float_side_perimeter(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10)
    def test_negative_float_sides_perimeter(self):
        res = perimeter(-2.5)
        self.assertEqual(res, "IllegalArgumentException")

    def test_big_integer_area(self):
        res = area(10**40)
        self.assertEqual(res, 10**80)
    def test_big_integer_perimeter(self):
        res = perimeter(10**40)
        self.assertEqual(res, 4 * 10**40)
    
    def test_string_area(self):
        res = area("xd")
        self.assertEqual(res, "IllegalArgumentException")
    def test_string_perimeter(self):
        res = perimeter("xd")
        self.assertEqual(res, "IllegalArgumentException")