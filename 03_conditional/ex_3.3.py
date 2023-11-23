# score = input('Enter score: ')
# try:
#     score = float(score)
#     if 0.0 <= score < 0.6:
#         print('F')
#     elif score < 0.7:
#         print('D')
#     elif score < 0.8:
#         print('C')
#     elif score < 0.9:
#         print('B')
#     elif score <= 1:
#         print('A')
#     else:
#         print('Bad score')
# except ValueError:
#     print('Bad score')

# Second variant with 'quit()'
score = input('Enter score: ')

try:
    s = float(score)
except ValueError:
    print('Bad score')
    quit()

if 0.0 <= s < 0.6:
    print('F')
elif s < 0.7:
    print('D')
elif s < 0.8:
    print('C')
elif s < 0.9:
    print('B')
elif s <= 1:
    print('A')
else:
    print('Bad score')
