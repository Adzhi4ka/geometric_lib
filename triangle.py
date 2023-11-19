import unittest

def area(a, h):
    '''
        Возвращает площадь треугольника с известной длинной стороны и высоту, опущенной к этой стороне

            Параметры:
                a (float): длина стороны треугольника
                h (float): длина высоты трегольника

            Возвращаемое значение:
                a * h / 2 (float): площадь треугольника

            Примеры работы:
                area(1.0, 2.0) = 1.0
                area(0.5, 3.0) = 0.75
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
        Возвращает периметр треугольника с известными длиннами всех сторон

            Параметры:
                a (float): длина первой стороны треугольника
                b (float): длина второй стороны трегольника
                c (float): длина третей стороны треугольника

            Возвращаемое значение:
                a + b + c (float): периметр треугольника
            
            Примеры работы:
                perimeter(1.0, 2.0, 3.0) = 6.0
                perimeter(0.5, 3.5, 3.0) = 7.0
    '''
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_positive_integer_area(self):
        res = area(5, 4)
        self.assertEqual(res, 10)
    def test_negative_integer_area(self):
        res = area(-5, -4)
        self.assertEqual(res, "UncorrectValue")
    def test_negative_and_positive_integer_area(self):
        res = area(-5, 4)
        self.assertEqual(res, "UncorrectValue")
    
    def test_positive_integer_perimeter(self):
        res = perimeter(5, 4, 3)
        self.assertEqual(res, 12)
    def test_negative_integer_perimeter(self):
        res = perimeter(-5, -4, -3)
        self.assertEqual(res, "UncorrectValue")
    def test_1_negative_2_positive_3_negative_integer_perimeter(self):
        res = perimeter(-5, 4, -3)
        self.assertEqual(res, "UncorrectValue")
    def test_1_positive_2_negative_3_negative_perimeter(self):
        res = perimeter(5, -4, -3)
        self.assertEqual(res, "UncorrectValue")
    def test_1_negative_2_negative_3_positive_perimeter(self):
        res = perimeter(-5, -4, 3)
        self.assertEqual(res, "UncorrectValue")
    def test_1_negative_2_positive_3_positive_perimeter(self):
        res = perimeter(-5, 4, 3)
        self.assertEqual(res, "UncorrectValue")

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
        self.assertEqual(res, "UncorrectValueType")
    def test_string_perimeter(self):
        res = area("xd", "xdxd", "xdxdxd")
        self.assertEqual(res, "UncorrectValueType")
