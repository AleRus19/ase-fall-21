import unittest
import calculator as c


class TestDivide(unittest.TestCase):

    def test_divide_integers_positive(self):
        result = c.divide(6, 3)
        self.assertEqual(result, 2)

    def test_divide_integers_positive2(self):
        result = c.divide(7, 3)
        self.assertEqual(result, 2)

    def test_divide_integers_negative(self):
        result = c.divide(-6, -2)
        self.assertEqual(result, 3)

    def test_divide_integers_negative2(self):
        result = c.divide(-7, -2)
        self.assertEqual(result, 3)

    def test_divide_integers_pos_neg(self):
        result = c.divide(6, -2)
        self.assertEqual(result, -3)

    def test_divide_integers_pos_neg2(self):
        result = c.divide(9, -2)
        self.assertEqual(result, -4)

    def test_divide_integers_neg_pos(self):
        result = c.divide(-6, 2)
        self.assertEqual(result, -3)

    def test_divide_integers_neg_pos2(self):
        result = c.divide(-7, 2)
        self.assertEqual(result, -3)

    def test_divide_zero(self):
        result = c.divide(0, 2)
        self.assertEqual(result, 0)

    def test_divide_by_zero(self):
        self.assertRaises(ZeroDivisionError, c.divide, 6, 0)


if __name__ == '__main__':
    unittest.main()
