import unittest

def area(a, b):
    return a * b 

def perimeter(a, b):
    return 2 * a + 2 * b 


class RectangleTestCase(unittest.TestCase):
    def test_positive_integer_sides_area(self):
        res = area(2, 5)
        self.assertEqual(res, 10)
    def test_negative_integer_sides_area(self):
        res = area(-2, -5)
        self.assertEqual(res, "IllegalArgumentException")
    def test_negative_and_positive_integer_sides_area(self):
        res = area(-2, 5)
        self.assertEqual(res, "IllegalArgumentException")

    def test_positive_integer_sides_perimeter(self):
        res = perimeter(2, 5)
        self.assertEqual(res, 14)
    def test_negative_integer_sides_perimeter(self):
        res = perimeter(-2, -5)
        self.assertEqual(res, "IllegalArgumentException")
    def test_negative_and_positive_sides_integer_perimeter(self):
        res = perimeter(-2, 5)
        self.assertEqual(res, "IllegalArgumentException")

    def test_positive_float_sides_area(self):
        res = area(2.5, 3.5)
        self.assertEqual(res, 8.75)
    def test_negative_float_sides_area(self):
        res = area(-2.5, -5.5)
        self.assertEqual(res, "IllegalArgumentException")
    def test_negative_and_positive_float_sides_area(self):
        res = area(-2.5, 5.5)
        self.assertEqual(res, "IllegalArgumentException")

    def test_positive_float_sides_perimeter(self):
        res = perimeter(2.5, 3.5)
        self.assertEqual(res, 12)
    def test_negative_float_sides_perimeter(self):
        res = perimeter(-2.5, -5.5)
        self.assertEqual(res, "IllegalArgumentException")
    def test_negative_and_positive_float_sides_perimeter(self):
        res = perimeter(-2.5, 5.5)
        self.assertEqual(res, "IllegalArgumentException")
    
    def test_big_integer_area(self):
        res = area(2 ** 20, 5 ** 20)
        self.assertEqual(res, 10 ** 20)
    def test_big_integer_perimeter(self):
        res = perimeter(2 ** 20, 5 ** 20)
        self.assertEqual(res, 190734865378402)
    
    def test_string_area(self):
        res = area("xd", "xdxd")
        self.assertEqual(res, "IllegalArgumentException")
    def test_string_perimeter(self):
        res = perimeter("xd", "xdxd")
        self.assertEqual(res, "IllegalArgumentException")