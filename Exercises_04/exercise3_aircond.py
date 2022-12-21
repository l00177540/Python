celsius_conversion = 273.15
# List of 10 temperature values in Kelvin
kelvin_value = [280, 290, -273, 291, 292, 293, 294, 297, 298, 300]
# Convert to Celsius
celsius_value = [(kelvin - celsius_conversion) for kelvin in kelvin_value] 
# Convert to Fahrenheit
fahrenheit_value = [(celsius * 1.8 + 32) for celsius in celsius_value]
# Print 3 distinct lines with K, degrees C and degrees F
print(f"The 10 values in K are: {kelvin_value}\n")
print(f"The equivalent 10 values in Degrees C are: {celsius_value}\n")
print(f"The equivalent 10 values in Degrees F are: {fahrenheit_value}\n")
