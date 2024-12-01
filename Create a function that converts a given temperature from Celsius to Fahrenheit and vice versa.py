def convert_temperature(x, unit):
    if unit == 'C':
        # Convert Celsius to Fahrenheit
        return (x * 9/5) + 32
    elif unit == 'F':
        # Convert Fahrenheit to Celsius
        return (x - 32) * 5/9
    else:
        return "Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit."

celsius = 25
fahrenheit = convert_temperature(celsius, 'C')
print(f"{celsius}°C is equal to {fahrenheit}°F")

fahrenheit_value = 77
celsius_value = convert_temperature(fahrenheit_value, 'F')
print(f"{fahrenheit_value}°F is equal to {celsius_value}°C")
