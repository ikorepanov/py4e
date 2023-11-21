def evaluate_payment(hours, rate):
    """
    Calculate the payment based on the number of hours worked and the hourly
    rate: 1.5 times the hourly rate for hours worked above 40 hours.
    """
    try:
        h = float(hours)
        r = float(rate)
        if h > 40:
            h = 40 + (h - 40) * 1.5
        payment = round(h * r, 2)
        return f'Pay: {payment}'
    except ValueError:
        return (
            'Invalid input. Please enter numeric values for hours and (or) '
            'rate.'
        )


hours = input('Enter Hours: ')
rate = input('Enter Rate: ')

print(evaluate_payment(hours, rate))
