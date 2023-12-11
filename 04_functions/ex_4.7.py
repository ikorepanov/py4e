def computegrade(score):
    """
    Compute the grade based on the provided score.
    """
    try:
        s = float(score)
    except ValueError:
        print('Bad score')
        quit()

    if 0.0 <= s < 0.6:
        grade = 'F'
    elif s < 0.7:
        grade = 'D'
    elif s < 0.8:
        grade = 'C'
    elif s < 0.9:
        grade = 'B'
    elif s <= 1:
        grade = 'A'
    else:
        grade = 'Bad score'

    return grade


score = input('Enter score: ')
print(computegrade(score))
