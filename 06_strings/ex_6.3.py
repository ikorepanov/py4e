# def count(some):
#     count = 0
#     try:
#         string, letter = some.split()
#         for char in string:
#             if char == letter:
#                 count += 1
#         print(count)
#     except ValueError:
#         print('You forget enter string or letter')


# some = input('Enter string and letter: \n')
# count(some)

def count_letters():
    """
    Count the number of a certain letter in a string.
    """
    count = 0
    while True:
        some = input('Enter string and letter: \n')
        try:
            string, letter = some.split()
        except ValueError:
            print('You forget to enter a string or letter or make incorrect '
                  'input: need one string and one letter with a comma or a '
                  'space in between')
            continue
        for symbol in string:
            if symbol == letter:
                count += 1
        break
    print('Result is:', count)


count_letters()
