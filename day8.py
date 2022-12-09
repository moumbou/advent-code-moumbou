import numpy as np
file = open('info.txt', 'r')
info = file.readlines()
file.close()

mat = []
for line in info:
    line = line.replace('\n', '')
    mat.append(line)

x = len(mat[0])
y = len(mat)

matrice = np.zeros((y, x))

for i, _ in enumerate(range(x)):
    for j, _ in enumerate(range(y)):
        el = mat[i]
        matrice[i][j] = el[j]

trees = 0
positions = []
for i, _ in enumerate(range(x)):
    for j, _ in enumerate(range(y)):
        if i != 0 and j != 0 and i != x - 1 and j != y - 1:
            onSearch = True
            ii = i
            jj = j
            top, bottom, left, right = (True, True, True, True)
            while onSearch:
                # top
                while top:
                    ii -= 1
                    if ii >= 0:
                        if matrice[i][j] <= matrice[ii][jj]:
                            top = False
                            break
                    else:
                        if (i, j) not in positions:
                            positions.append((i, j))
                        onSearch = False
                        break

                # bottom
                ii = i
                while bottom:
                    ii += 1
                    if ii <= y-1:
                        if matrice[i][j] <= matrice[ii][jj]:
                            bottom = False
                            break
                    else:
                        if (i, j) not in positions:
                            positions.append((i, j))
                        onSearch = False
                        break

                # left
                ii = i
                while left:
                    jj -= 1
                    if jj >= 0:
                        if matrice[i][j] <= matrice[ii][jj]:
                            left = False
                            break
                    else:
                        if (i, j) not in positions:
                            positions.append((i, j))
                        onSearch = False
                        break

                # right
                ii = i
                jj = j
                while right:
                    jj += 1
                    if jj <= x - 1:
                        if matrice[i][j] <= matrice[ii][jj]:
                            right = False
                            break
                    else:
                        if (i, j) not in positions:
                            positions.append((i, j))
                        onSearch = False
                        break
                onSearch = False


edges = (x * 2) + (y - 2) * 2
# PART ONE
print(edges + len(positions))

# PART TWO
scores = []
for position in positions:
    onSearch = True
    i, j = position
    ii, jj = position
    top, bottom, left, right = (True, True, True, True)
    t, r, l, b = (0, 0, 0, 0)

    # top
    while top:
        ii -= 1
        if ii >= 0:
            if matrice[i][j] > matrice[ii][jj]:
                t += 1
            else:
                t += 1
                top = False
                break
        else:
            break

    # bottom
    ii = i
    while bottom:
        ii += 1
        if ii <= y - 1:
            if matrice[i][j] > matrice[ii][jj]:
                b += 1
            else:
                b += 1
                bottom = False
                break
        else:
            break

    # left
    ii = i
    while left:
        jj -= 1
        if jj >= 0:
            if matrice[i][j] > matrice[ii][jj]:
                l += 1
            else:
                l += 1
                left = False
                break
        else:
            break

    # right
    ii = i
    jj = j
    while right:
        jj += 1
        if jj <= x - 1:
            if matrice[i][j] > matrice[ii][jj]:
                r += 1
            else:
                r += 1
                right = False
                break
        else:
            break
    
    score = t*r*l*b
    scores.append(score)
scores.sort(reverse=True)
print(scores[0])

"""
Example

30373
25512
65332
33549
35390

"""