import math
import unittest

def area(r):
    '''
    Возвращает площадь круга с известной длинной радиуса
        
        Параметры:
            r (float): радиус круга
        
        Возвращаемое значение:
            math.pi * r * r (float): площадь круга

        Примеры использования:
            area(1.0) = 3.14159256
            area(0.5) = 0.78539816
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга с известной длинной радиуса

        Параметры:
            r (float): радиус круга
        
        Возвращаемое значение:
            2 * math.pi * r (float): периметр круга

        Примеры использования:
            perimeter(1.0) = 6.28318531
            perimeter(0.5) = 3.14159256
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):

    def test_positive_integer_radius_area(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)
    def test_negative_integer_radius_area(self):
        res = area(-10)
        self.assertEqual(res, "UncorrectValue")

    def test_positive_integer_radius_perimetr(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)
    def test_negative_integer_radius_perimetr(self):
        res = perimeter(-10)
        self.assertEqual(res, "UncorrectValue")

    def test_positive_float_radius_area(self):
        res = area(2.5)
        self.assertEqual(res, 19.634954084936208)
    def test_negative_float_radius_area(self):
        res = area(-2.5)
        self.assertEqual(res, "UncorrectValue")

    def test_positive_float_radius_perimetr(self):
        res = perimeter(c)
        self.assertEqual(res, 15.707963267948966)
    def test_negative_float_radius_perimetr(self):
        res = perimeter(-2.5)
        self.assertEqual(res, "UncorrectValue")

    def test_string_radius_area(self):
        res = area("XDXDXD")
        self.assertEqual(res, "UncorrectValueType")
    def test_string_radius_perimetr(self):
        res = perimeter("XDXDXD")
        self.assertEqual(res, "UncorrectValueType")

    def test_big_int_radius_area(self):
        res = area(10**20)
        self.assertEqual(res, 3.141592653589793e+40)
    def test_big_int_radius_perimetr(self):
        res = perimeter(5 * 10**19)
        self.assertEqual(res, 3.1415926535897933e+20)
