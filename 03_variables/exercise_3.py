def evaluate_payment(hours, rate):
    hours = float(hours)
    rate = float(rate)
    return round(hours * rate, 2)


hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

print(f'Pay: {evaluate_payment(hours, rate)}')

# ChatGPT version:

# def evaluate_payment(hours, rate):
#     """
#     Calculate the payment based on the number of hours worked and the hourly rate.

#     Args:
#         hours (str or float): The number of hours worked.
#         rate (str or float): The hourly rate.

#     Returns:
#         float: The calculated payment rounded to the nearest cent.
#                If the input is not a valid numeric value, returns an error message.
#     """
#     try:
#         hours = float(hours)
#         rate = float(rate)
#         payment = hours * rate
#         return round(payment, 2)
#     except ValueError:
#         return "Invalid input. Please enter numeric values for hours and rate."

# def main():
#     hours = input('Enter Hours: ')
#     rate = input('Enter Rate: ')

#     result = evaluate_payment(hours, rate)
#     print(f'Pay: {result}')

# if __name__ == "__main__":
#     main()