# Let's import everything from conversion
from conversions import *
from conversions_refactored import convert

import unittest


class ConversionTest(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        celsius = 0
        result = convertCelsiusToKelvin(0)
        expected = 273.15
        self.assertEqual(result, expected)

        result = convertCelsiusToKelvin(300)
        expected = 573.15
        self.assertEqual(result, expected)
       
        result = convertCelsiusToKelvin(100)
        expected = 373.15
        self.assertEqual(result, expected)
      
        result = convertCelsiusToKelvin(55)
        expected = 328.15
        self.assertEqual(result, expected)
       
        result = convertCelsiusToKelvin(88)
        expected = 361.15
        self.assertEqual(result, expected)

    def test_convertCelsiusToFahrenheit(self):
        celsius = 0
        result = convertCelsiusToFahrenheit(0)
        expected = 32
        self.assertEqual(result, expected)

        result = convertCelsiusToFahrenheit(21)
        expected = 69.8
        self.assertEqual(result, expected)
      
        result = convertCelsiusToFahrenheit(55)
        expected = 131
        self.assertEqual(result, expected)
       
        result = convertCelsiusToFahrenheit(80)
        expected = 176
        self.assertEqual(result, expected)
       
        result = convertCelsiusToFahrenheit(250)
        expected = 482
        self.assertEqual(result, expected)

    def test_convertFahrenheitToCelsius(self):
        celsius = 0
        result = convertFahrenheitToCelsius(32)
        expected = 0
        self.assertEqual(result, expected)

        result = convertFahrenheitToCelsius(40)
        expected = 4.444444
        self.assertAlmostEqual(result, expected, places=6)
      
        result = convertFahrenheitToCelsius(77)
        expected = 25
        self.assertEqual(result, expected)
      
        result = convertFahrenheitToCelsius(41)
        expected = 5
        self.assertEqual(result, expected)
      
        result = convertFahrenheitToCelsius(95)
        expected = 35
        self.assertEqual(result, expected)
      
    def test_convertFahrenheitToKelvin(self):
        celsius = 0
        result = convertFahrenheitToKelvin(32)
        expected = 273.15
        self.assertEqual(result, expected)

        result = convertFahrenheitToKelvin(5)
        expected = 258.15
        self.assertEqual(result, expected)
      
        result = convertFahrenheitToKelvin(77)
        expected = 298.15
        self.assertEqual(result, expected)
      
        result = convertFahrenheitToKelvin(41)
        expected = 278.15
        self.assertEqual(result, expected)
      
        result = convertFahrenheitToKelvin(95)
        expected = 308.15
        self.assertEqual(result, expected)

    def test_convertKelvinToCelsius(self):
        celsius = 0
        result = convertKelvinToCelsius(0)
        expected = -273.15
        self.assertEqual(result, expected)

        result = convertKelvinToCelsius(300)
        expected = 26.58
        self.assertEqual(result, expected)
       
        result = convertKelvinToCelsius(500)
        expected = 226.85
        self.assertEqual(result, expected)
      
        result = convertKelvinToCelsius(320)
        expected = 46.85
        self.assertEqual(result, expected)
       
        result = convertKelvinToCelsius(88)
        expected = -185.15
        self.assertEqual(result, expected)

    def test_convertKelvinToFahrenheit(self):
        celsius = 0
        result = convertKelvinToFahrenheit(0)
        expected = -459.67
        self.assertEqual(result, expected)

        result = convertKelvinToFahrenheit(300)
        expected = 80.33
        self.assertEqual(result, expected)
       
        result = convertKelvinToFahrenheit(500)
        expected = 440.33
        self.assertEqual(result, expected)
      
        result = convertKelvinToFahrenheit(320)
        expected = 116.33
        self.assertEqual(result, expected)
       
        result = convertKelvinToFahrenheit(88)
        expected = -301.27
        self.assertEqual(result, expected)

    def test_convert(self):
        celsius = 0
        result = convert("Celsius", "Kelvin", celsius)
        expected = 273.15
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
