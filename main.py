while True:
    print("Temperature: " + input.temperature(TemperatureUnit.FAHRENHEIT))
    if input.temperature(TemperatureUnit.FAHRENHEIT) > 70:
        light.set_all(light.rgb(250, 0, 0))
    elif input.temperature(TemperatureUnit.FAHRENHEIT) < 70 and input.temperature(TemperatureUnit.FAHRENHEIT) > 40:
        light.set_all(light.rgb(0, 250, 0))
    else:
        light.set_all(light.rgb(0, 0, 250))