import unittest
import calculator as c


class TestMultiply(unittest.TestCase):

    def test_multiply_integers_positive(self):
        result = c.multiply(6, 3)
        self.assertEqual(result, 18)

    def test_multiply_integers_positive2(self):
        result = c.multiply(7, 3)
        self.assertEqual(result, 21)

    def test_multiply_integers_negative(self):
        result = c.multiply(-6, -2)
        self.assertEqual(result, 12)

    def test_multiply_integers_negative2(self):
        result = c.multiply(-7, -2)
        self.assertEqual(result, 14)

    def test_multiply_integers_pos_neg(self):
        result = c.multiply(6, -2)
        self.assertEqual(result, -12)

    def test_multiply_integers_pos_neg2(self):
        result = c.multiply(9, -2)
        self.assertEqual(result, -18)

    def test_multiply_integers_neg_pos(self):
        result = c.multiply(-6, 2)
        self.assertEqual(result, -12)

    def test_multiply_integers_neg_pos2(self):
        result = c.multiply(-7, 2)
        self.assertEqual(result, -14)

    def test_multiply_zero(self):
        result = c.multiply(0, 2)
        self.assertEqual(result, 0)

    def test_multiply_zero2(self):
        result = c.multiply(3, 0)
        self.assertEqual(result, 0)

    def test_multiply_zero3(self):
        result = c.multiply(-3, 0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
