try:
    h = float(input('Enter Hours: '))
    r = float(input('Enter Rate: '))
    if h > 40:
        h = 40 + (h - 40) * 1.5
    payment = round(h * r, 2)
    print(f'Pay: {payment}')
except ValueError:
    print('Error, please enter numeric input')


# Second variant with 'quit()'
try:
    h = float(input('Enter Hours: '))
    r = float(input('Enter Rate: '))
except ValueError:
    print('Error, please enter numeric input')
    quit()

if h > 40:
    h = 40 + (h - 40) * 1.5
payment = round(h * r, 2)
print(f'Pay: {payment}')
