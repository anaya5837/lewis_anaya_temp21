temp = input.temperature(TemperatureUnit.FAHRENHEIT)
while True:
    print("Temperature: " + temp)
    if temp > 60:
        light.set_pixel_color(4, light.rgb(250, 0, 0))
    else:
        light.clear()