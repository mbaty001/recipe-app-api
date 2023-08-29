from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add(self):

        self.assertEqual(calc.add(5, 6), 11)

    def test_subtract(self):

        self.assertAlmostEqual(calc.substract(10, 15), 5)
