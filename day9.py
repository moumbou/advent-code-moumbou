import numpy as np
file = open('info.txt', 'r')
info = file.readlines()
file.close()

y = 500 
x = 500
matrice = np.zeros((y,x))
startingPoint = [int(x/2),int(y/2)]

matrice[startingPoint[0]][startingPoint[1]] = 3
PositionsH = [(startingPoint[0], startingPoint[1])]
PositionsT = [(startingPoint[0], startingPoint[1])]
Positions1 = [(startingPoint[0], startingPoint[1])]
Positions2 = [(startingPoint[0], startingPoint[1])]
Positions3 = [(startingPoint[0], startingPoint[1])]
Positions4 = [(startingPoint[0], startingPoint[1])]
Positions5 = [(startingPoint[0], startingPoint[1])]
Positions6 = [(startingPoint[0], startingPoint[1])]
Positions7 = [(startingPoint[0], startingPoint[1])]
Positions8 = [(startingPoint[0], startingPoint[1])]
Positions9 = [(startingPoint[0], startingPoint[1])]

# PART ONE
def compare(T,H):
    i,j = H
    ii,jj = T
    resultI = 0
    resultJ = 0
    if i > ii:
        resultI = i - ii
    else:
        resultI = ii - i
    if j > jj:
        resultJ = j - jj
    else:
        resultJ = jj - j

    if resultJ <= 1 and resultI <= 1:
        return None
    else:
        resultI = i - ii
        resultJ = j - jj
        if resultJ == -2 or resultJ == 2:
            if resultJ > 0:
                return (i, j - 1)
            else:
                return (i, j + 1)
        else:
            if resultI < 0:
                return (i + 1, j)
            else:
                return (i - 1, j)

for instruction in info:
    instruction = instruction.replace('\n', '')
    direction, mount = instruction.split()
    for _ in range(int(mount)):
        lastPostionH = PositionsH[len(PositionsH) - 1]
        lastPostionT = PositionsT[len(PositionsT) - 1]
        if direction == 'U':
            i,j = lastPostionH
            i -= 1
            PositionsH.append((i, j))
            afterCompare = compare(lastPostionT, (i, j))
            if afterCompare:
                PositionsT.append(afterCompare)
        elif direction == 'D':
            i,j = lastPostionH
            i += 1
            PositionsH.append((i, j))
            afterCompare = compare(lastPostionT, (i, j))
            if afterCompare:
                PositionsT.append(afterCompare)
        elif direction == 'L':
            i,j = lastPostionH
            j -= 1
            PositionsH.append((i, j))
            afterCompare = compare(lastPostionT, (i, j))
            if afterCompare:
                PositionsT.append(afterCompare)
        else:
            i,j = lastPostionH
            j += 1
            PositionsH.append((i, j))
            afterCompare = compare(lastPostionT, (i, j))
            if afterCompare:
                PositionsT.append(afterCompare)

# PositionsTCleaned = []
# for p in PositionsT:
#     if p not in PositionsTCleaned:
#         PositionsTCleaned.append(p)
# print(len(PositionsT))

# PART TWO
for p in PositionsH:
    lastP1 = Positions1[len(Positions1) - 1]
    lastP2 = Positions2[len(Positions2) - 1]
    lastP3 = Positions3[len(Positions3) - 1]
    lastP4 = Positions4[len(Positions4) - 1]
    lastP5 = Positions5[len(Positions5) - 1]
    lastP6 = Positions6[len(Positions6) - 1]
    lastP7 = Positions7[len(Positions7) - 1]
    lastP8 = Positions8[len(Positions8) - 1]
    lastP9 = Positions9[len(Positions9) - 1]
    result = compare(lastP1, p)
    if result:
        Positions1.append(result)
        result = compare(lastP2, result)
        if result:
            Positions2.append(result)
            result = compare(lastP3, result)
            if result:
                Positions3.append(result)
                result = compare(lastP4, result)
                if result:
                    Positions4.append(result)
                    result = compare(lastP5, result)
                    if result:
                        Positions5.append(result)
                        result = compare(lastP6, result)
                        if result:
                            Positions6.append(result)
                            result = compare(lastP7, result)
                            if result:
                                Positions7.append(result)
                                result = compare(lastP8, result)
                                if result:
                                    Positions8.append(result)
                                    result = compare(lastP9, result)
                                    if result:
                                        Positions9.append(result)

Positions9Cleaned = []
for p in Positions9:
    if p not in Positions9Cleaned:
        Positions9Cleaned.append(p)
print(len(Positions9Cleaned))

"""

! PS : part two dosn't work for me but the example i made it with drawing you can use numpy to draw as matrice .

EXAMPLE:

R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20

"""