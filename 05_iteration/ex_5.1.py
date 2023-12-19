def some():
    """
    Enter docstring here(!).
    """
    # number = None  # Первый вариант. Работает!
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

    number = None  # Второй вариант. Работает!
    total = 0
    count = 0
    average = 0
    while number != 'done':
        number = input('Enter a number: ')
        if number != 'done':
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
