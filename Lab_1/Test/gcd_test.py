import unittest
import calculator as c
import math


class TestGcd(unittest.TestCase):

    def test_gcd_integers_positive(self):
        result = c.gcd(6, 3)
        self.assertEqual(result, math.gcd(6, 3))

    def test_gcd_integers_positive2(self):
        result = c.gcd(6, 12)
        self.assertEqual(result, math.gcd(6, 12))

    def test_gcd_integers_positive3(self):
        result = c.gcd(12, 36)
        self.assertEqual(result, math.gcd(12, 36))

    def test_gcd_integers_no_gcd(self):
        result = c.gcd(12, 5)
        self.assertEqual(result, math.gcd(12, 5))

    def test_gcd_integers_negative(self):
        result = c.gcd(-12, -36)
        self.assertEqual(result, math.gcd(-12, -36))

    def test_gcd_integers_pos_neg(self):
        result = c.gcd(12, -36)
        self.assertEqual(result, math.gcd(12, -36))

    def test_gcd_integers_zero(self):
        result = c.gcd(10, 0)
        self.assertEqual(result, math.gcd(10, 0))

    def test_gcd_integers_zero2(self):
        result = c.gcd(0, 34)
        self.assertEqual(result, math.gcd(0, 34))

    def test_gcd_integers_zero3(self):
        result = c.gcd(0, 0)
        self.assertEqual(result, math.gcd(0, 0))


if __name__ == '__main__':
    unittest.main()
