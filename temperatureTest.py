import unittest
from temperatureConverter import *

class TestTemperature(unittest.TestCase):
    def test_convertCelciusToFahrenheit(self):
        self.assertEqual(32, convertCelciusToFahrenheit(0))
        self.assertEqual(212, convertCelciusToFahrenheit(100))

    def test_convertCelciusToKelvin(self):
        self.assertEqual(273, convertCelciusToKelvin(0))
        self.assertEqual(373, convertCelciusToKelvin(100))

    def test_convertFahrenheitToCelcius(self):
        self.assertEqual(0, convertFahrenheitToCelcius(32))
        self.assertEqual(100, convertFahrenheitToCelcius(212))

    def test_convertFahrenheitToKelvin(self):
        self.assertEqual(273, convertFahrenheitToKelvin(32))
        self.assertEqual(373, convertFahrenheitToKelvin(212))

    def test_convertKelvinToCelcius(self):
        self.assertEqual(0, convertKelvinToCelcius(273))
        self.assertEqual(100, convertKelvinToCelcius(373))

    def test_convertKelvinToFahrenheit(self):
        self.assertEqual(32, convertKelvinToFahrenheit(273))
        self.assertEqual(212, convertKelvinToFahrenheit(373))

if __name__ == '__main__':
    unittest.main()