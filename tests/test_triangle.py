import unittest

def area(a, h):
    return a * h / 2 

def perimeter(a, b, c):
    return a + b + c 

class TriangleTestCase(unittest.TestCase):
    def test_positive_integer_area(self):
        res = area(5, 4)
        self.assertEqual(res, 10)
    def test_negative_integer_area(self):
        res = area(-5, -4)
        self.assertEqual(res, "IllegalArgumentException")
    def test_negative_and_positive_integer_area(self):
        res = area(-5, 4)
        self.assertEqual(res, "IllegalArgumentException")
    
    def test_positive_integer_perimeter(self):
        res = perimeter(5, 4, 3)
        self.assertEqual(res, 12)
    def test_negative_integer_perimeter(self):
        res = perimeter(-5, -4, -3)
        self.assertEqual(res, "IllegalArgumentException")
    def test_1_negative_2_positive_3_negative_integer_perimeter(self):
        res = perimeter(-5, 4, -3)
        self.assertEqual(res, "IllegalArgumentException")
    def test_1_positive_2_negative_3_negative_perimeter(self):
        res = perimeter(5, -4, -3)
        self.assertEqual(res, "IllegalArgumentException")
    def test_1_negative_2_negative_3_positive_perimeter(self):
        res = perimeter(-5, -4, 3)
        self.assertEqual(res, "IllegalArgumentException")
    def test_1_negative_2_positive_3_positive_perimeter(self):
        res = perimeter(-5, 4, 3)
        self.assertEqual(res, "IllegalArgumentException")

    def test_float_area(self):
        res = area(2.5, 4)
        self.assertEqual(res, 5)
    def test_integer_perimeter(self):
        res = perimeter(2.5, 3.3, 5.3)
        self.assertEqual(res, 11.1)
    
    def test_big_int_area(self):
        res = area(2 ** 31, 5 ** 30)
        self.assertEqual(res, 1e+30)
    def test_big_int_perimeter(self):
        res = perimeter(10 ** 40, 10 ** 41, 10 ** 42)
        self.assertEqual(res, 111 * 10 ** 40)
    
    def test_string_area(self):
        res = area("xd", "xdxd")
        self.assertEqual(res, "IllegalArgumentException")
    def test_string_perimeter(self):
        res = area("xd", "xdxd", "xdxdxd")
        self.assertEqual(res, "IllegalArgumentException")