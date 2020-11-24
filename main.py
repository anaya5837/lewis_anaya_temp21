temp = input.temperature(TemperatureUnit.FAHRENHEIT)
while True:
    print("Temperature: " + temp)
    if temp > 70:
        light.set_all(light.rgb(250, 0, 0))
    elif temp < 70 and temp > 40:
        light.set_all(light.rgb(0, 250, 0))
    else:
        light.set_all(light.rgb(0, 0, 250))