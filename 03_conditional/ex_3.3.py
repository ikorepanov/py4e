score = input('Enter score: ')
try:
    score = float(score)
    if 0.0 <= score < 0.6:
        print('F')
    elif score < 0.7:
        print('D')
    elif score < 0.8:
        print('C')
    elif score < 0.9:
        print('B')
    elif score <= 1:
        print('A')
    else:
        print('Bad score')
except ValueError:
    print('Bad score')
