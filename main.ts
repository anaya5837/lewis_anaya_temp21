let temp = input.temperature(TemperatureUnit.Fahrenheit)
while (true) {
    console.log("Temperature: " + temp)
    if (temp > 70) {
        light.setAll(light.rgb(250, 0, 0))
    } else if (temp < 70 && temp > 40) {
        light.setAll(light.rgb(0, 250, 0))
    } else {
        light.setAll(light.rgb(0, 0, 250))
    }
    
}
