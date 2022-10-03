from conversions import *
class ConversionNotPossible(Exception):
	pass

def convert(from_units, to_units, value):

    from_lcase = from_units.lower()
    to_lcase = to_units.lower()

    # from Celsius to Kelvin and Fahrenheit
    if from_lcase == 'celsius' and to_lcase == "kelvin":
        return convertCelsiusToKelvin(value)
    elif from_lcase == 'celsius' and to_lcase == "fahrenheit":
        return convertCelsiusToFahrenheit(value)
    # from Kelvin to Celsius and Fahrenheit
    if from_lcase == 'kelvin' and to_lcase == "celsius":
        return convertKelvinToCelsius(value)
    elif from_lcase == 'kelvin' and to_lcase == "fahrenheit":
        return convertKelvinToFahrenheit(value)
    # from Fahrenheit to Celsius and Kelvin
    if from_lcase == 'fahrenheit' and to_lcase == "celsius":
        return convertFahrenheitToCelsius(value)
    elif from_lcase == 'fahrenheit' and to_lcase == "kelvin":
        return convertFahrenheittoKelvin(value)  
   
    # from Miles to Meters and Yards
    if from_lcase == 'miles' and to_lcase == "meters":
        return convertMilesToMeters(value)
    elif from_lcase == "miles" and to_lcase == "yards":
        return convertMilesToYards(value)
   # from Meters to Miles and Yards
    if from_lcase == 'meters' and to_lcase == "miles":
        return convertMetersToMiles(value)
    elif from_lcase == "meters" and to_lcase == "yards":
        return convertMetersToYards(value)
    # from Yards to Meters and Miles
    if from_lcase == 'yards' and to_lcase == "meters":
        return convertYardsToMeters(value)
    elif from_lcase == "yards" and to_lcase == "miles":
        return convertYardsToMiles(value)
    else:
		  raise ConversionNotPossible("Converting from incompatible units is not possible")
