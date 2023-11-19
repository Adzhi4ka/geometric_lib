import unittest

def area(a):
    '''
        Возвращает площадь квадрата с известной длинной стороны

            Параметры:
                a (float): длина стороны квадрата
        
            Возвращаемое значение:
                a * a (float): площадь квадрата

            Примеры работы:
                area(2.0) = 4.0
                area(0.5) = 0.25
    '''
    return a * a


def perimeter(a):
    '''
        Возвращает периметр квадрата с известной длинной стороны

            Параметры:
                a (float): длина стороны квадрата
        
            Возвращаемое значение:
                4 * a (float): периметр квадрата

            Примеры работы:
                perimeter(1.0) = 4
                perimeter(0.5) = 2
    '''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_positive_integer_side_area(self):
        res = area(2)
        self.assertEqual(res, 4)
    def test_negative_integer_sides_area(self):
        res = area(-2)
        self.assertEqual(res, "UncorrectValue")

    def test_positive_integer_side_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 8)
    def test_negative_integer_side_perimeter(self):
        res = perimeter(-2)
        self.assertEqual(res, "UncorrectValue")

    def test_positive_float_side_area(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)
    def test_negative_float_side_area(self):
        res = area(-2.5)
        self.assertEqual(res, "UncorrectValue")

    def test_positive_float_side_perimeter(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10)
    def test_negative_float_sides_perimeter(self):
        res = perimeter(-2.5)
        self.assertEqual(res, "UncorrectValue")

    def test_big_integer_area(self):
        res = area(10**40)
        self.assertEqual(res, 10**80)
    def test_big_integer_perimeter(self):
        res = perimeter(10**40)
        self.assertEqual(res, 4 * 10**40)
    
    def test_string_area(self):
        res = area("xd")
        self.assertEqual(res, "UncorrectValueType")
    def test_string_perimeter(self):
        res = perimeter("xd")
        self.assertEqual(res, "UncorrectValueType")
