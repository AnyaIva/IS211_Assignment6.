
_ZERO_C_IN_KELVIN = 273.15


def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = celsius + 273.15

    return kelvins


def convertCelsiusToFahrenheit(celsius):
    """
    Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit
    """
    fahrenheit = celsius * 9/5 + 32

    return fahrenheit


def convertFahrenheitToCelsius(fahrenheit):
    """
    Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit
    """
    result = (fahrenheit - 32) * 5/9

    return result


def convertFahrenheitToKelvin(fahrenheit):
    """
    Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit
    """
    result = (fahrenheit - 32) * 5/9 + 273.15

    return result


def convertKelvinToCelsius(kelvin):
    """
    Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit
    """
    result = kelvin - 273.15

    return result


def convertKelvintoFahrenheit(kelvin):
    """
    Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit
    """
    result = (kelvin - 273.15) * 9/5 + 32

    return result


def convertMilesToMeters(miles):
    """Convert Miles to Meters"""
    result = miles * 1609.34

    return result

def convertMilesToYards(miles):
    """Convert Miles to Yards """
    result = miles * 1760

    return result

def convertYardsToMiles(yards):
    """Convert Yards to Miles """
    result = yards / 1760

    return result

def convertYardsToMeters(yards):
    """Convert Yards to Meters """
    result = yards / 1.094

    return result

def convertMetersToMiles(meters):
    """Convert Meters to Miles """
    result = meters / 1609.34

    return result

def convertMetersToYards(meters):
    """Convert Meters to Yards """
    result = meters * 1.094

    return result
