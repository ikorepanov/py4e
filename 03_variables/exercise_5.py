def celsius_to_fahrenheit(temperature_celsius):
    temperature_celsius = float(temperature_celsius)
    return round(temperature_celsius * 9 / 5 + 32, 1)


temperature_celsius = input('Enter temperature in Celsius:\n')

print(
    f'Temperature in Fahrenheit is '
    f'{celsius_to_fahrenheit(temperature_celsius)}'
)

# ChatGPT version:

# # Constants for temperature conversion
# CELSIUS_TO_FAHRENHEIT_SCALE = 9/5
# CELSIUS_TO_FAHRENHEIT_OFFSET = 32

# def celsius_to_fahrenheit(temperature_celsius):
#     """
#     Convert a temperature from Celsius to Fahrenheit.

#     Args:
#         temperature_celsius (str or float): The temperature in Celsius to be converted.

#     Returns:
#         float: The temperature in Fahrenheit after the conversion.
#                If the input is not a valid numeric value, returns an error message.
#     """
#     try:
#         temperature_celsius = float(temperature_celsius)
#         fahrenheit = temperature_celsius * CELSIUS_TO_FAHRENHEIT_SCALE + CELSIUS_TO_FAHRENHEIT_OFFSET
#         return round(fahrenheit, 1)
#     except ValueError:
#         return "Invalid input. Please enter a numeric value for the temperature."

# def main():
#     temperature_celsius = input('Enter temperature in Celsius:\n')

#     result = celsius_to_fahrenheit(temperature_celsius)
#     print(f'Temperature in Fahrenheit is {result}')

# if __name__ == "__main__":
#     main()
