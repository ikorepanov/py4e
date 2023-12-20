def some():
    """
    Repeatedly read numbers until the user enters "done".
    Once "done" is entered, print out the total, count, and average of the
    numbers. If the user enters anything other than a number, detect their
    mistake using try and except and print an error message and skip to the
    next number.
    """
# Первый вариант
    # number = None
    # total = 0
    # count = 0
    # average = 0
    # while number != 'done':
    #     number = input('Enter a number: ')
    #     try:
    #         if number != 'done':
    #             n = float(number)
    #             total = total + n
    #             count = count + 1
    #             average = total / count
    #     except ValueError:
    #         print('Invalid input')
    #         continue
    # print(int(total), count, average)

# Второй вариант
    # number = None
    # total = 0
    # count = 0
    # average = 0
    # while number != 'done':
    #     number = input('Enter a number: ')
    #     if number != 'done':
    #         try:
    #             n = float(number)
    #         except ValueError:
    #             print('Invalid input')
    #             continue
    #         total = total + n
    #         count = count + 1
    #         average = total / count
    # print(int(total), count, average)

# Третий вариант (на основе Dr. Chuck's solution)
    count = 0
    total = 0
    average = 0  # Важно ввести эту переменную, т.к. тогда не будет ошибки ZeroDivisionError, если сразу ввести 'done'.
    while True:
        number = input('Enter a number: ')
        if number == 'done':
            break
        try:
            n = float(number)
        except ValueError:
            print('Invalid input')
            continue
        total = total + n
        count = count + 1
        average = total / count
    print(int(total), count, average)


some()
