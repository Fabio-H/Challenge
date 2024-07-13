print("Hello, we will now convert the temperature in Celsius and Fahrenheit")

C = int(input("Input the temperature in celsius: "))
F = int(input("Input the temperature in fahrenheit: "))

conversionF = (9/5 * int(C)) + 32
conversionC = 5/9 * (int(F) - 32)

print("Converting " + str(C) + "°C to Fahrenheit, results in: " + str(conversionF))
print("Converting " + str(F) + "°F to Celsius, results in: " + str(conversionC))