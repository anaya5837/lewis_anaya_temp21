let temp = input.temperature(TemperatureUnit.Fahrenheit)
while (true) {
    console.log("Temperature: " + temp)
    if (temp > 60) {
        light.setPixelColor(4, light.rgb(250, 0, 0))
    } else {
        light.clear()
    }
    
}
