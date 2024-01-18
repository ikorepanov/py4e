def count_letters():
    """
    Count the number of a certain letter in a string using string method
    'count'.
    """
    while True:
        some = input('Enter string and letter: \n')
        try:
            string, letter = some.split()
        except ValueError:
            print('You forget to enter a string or letter or make incorrect '
                  'input: need one string and one letter with a comma or a '
                  'space in between')
            continue
        break
    count = string.count(letter)

    print('Result is:', count)


def main():
    """
    Run the program when the module is running as a script (not as an imported
    module).
    """
    count_letters()


if __name__ == '__main__':
    main()
