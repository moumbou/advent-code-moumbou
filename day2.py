file = open('info.txt', 'r')
info = file.readlines()
file.close()

list = []
gameInfo = {'A': 'R', 'B': 'P', 'C': 'S', 'X': 'R', 'Y': 'P', 'Z': 'S'}
InfoForWin = {
    'S': 'R',
    'R': 'P',
    'P': 'S' 
}
infoForLoose = {
    'S': 'P',
    'R': 'S',
    'P': 'R'
}
# FOR THE SECONDE PART
newList = []
gameInfo2 = {'X': 'L', 'Y': 'D', 'Z': 'W'}
# --------------------
noteByHand = {'S': 3, 'R': 1, 'P': 2}
noteByResult = {'W': 6, 'L': 0, 'D': 3}
# FIRST PART
# for i in info:
#     text = i.replace('\n', '')
#     a, b = text.split()
#     list.append((gameInfo[a], gameInfo[b]))
# counter = 0
# for g in list:
#     a, b = g
#     noteByR = None
#     if a == b:
#         noteByR = 'D'
#     elif (a == 'R' and b == 'P') or (a == 'S' and b == 'R') or (a == 'P' and b == 'S'):
#         noteByR = 'W'
#     else:
#         noteByR = 'L'

#     counter += noteByHand[b] + noteByResult[noteByR]

#SECOND PART
counter = 0
for i in info:
    text = i.replace('\n', '')
    a, b = i.split()
    a = gameInfo[a]
    x = gameInfo2[b]
    y = None
    if x == 'D':
        y = a
    elif x == 'W':
        y = InfoForWin[a]
    else:
        y = infoForLoose[a]
    
    counter += noteByResult[x] + noteByHand[y]

print(counter)

"""
EXAMPLE

A Y
A Z
A X
B X
A Y
B Y
B Y
A X
A Z
A X
A X
A X
B X
B X
B X
B X
C Z
B Z
B Y
B X
A X

"""