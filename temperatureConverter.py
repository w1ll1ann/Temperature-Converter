def convertCelciusToFahrenheit(temperatureCelsius):
    return temperatureCelsius * 9/5 + 32

def convertCelciusToKelvin(temperatureCelsius):
    return temperatureCelsius + 273

def convertFahrenheitToCelcius(temperatureFahrenheit):
    return (temperatureFahrenheit - 32) * 5/9

def convertFahrenheitToKelvin(temperatureFahrenheit):
    return convertFahrenheitToCelcius(temperatureFahrenheit) + 273

def convertKelvinToCelcius(temperatureKelvin):
    return temperatureKelvin - 273

def convertKelvinToFahrenheit(temperatureKelvin):
    return convertCelciusToFahrenheit(temperatureKelvin - 273)

if __name__ == '__main__':
    pass