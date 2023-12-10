def computepay(hours, rate):
    """
    Calculate the payment based on the number of hours worked and the hourly
    rate.
    """
    try:
        hours = float(hours)
        rate = float(rate)
    except ValueError:
        print('Input correct number')
        quit()

    if hours > 40:
        hours = (hours - 40) * 1.5 + 40
    pay = round(hours * rate, 2)
    return pay


hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
payment = computepay(hours, rate)

print(f'Pay: {payment}')
