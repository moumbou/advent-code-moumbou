import numpy as np
file = open('info.txt', 'r')
info = file.readlines()
file.close()

textToRemove = ['move ', ' from', ' to', '\n']

rools = []
arrays = []
isArrayInfo = True
for text in info:
    text = text.replace('\n', '')
    if len(text) and isArrayInfo:
        text = text.replace('[', ' ')
        text = text.replace(']', ' ')
        arrays.append(text)
    else:
        isArrayInfo = False
    if not isArrayInfo and len(text):
        rools.append(text)

indexes = arrays.pop(len(arrays) - 1)
indexesEl = indexes.split()
indexesPlacement = {}
for ind in indexesEl:
    for i,el in enumerate(indexes):
        if ind == el:
            indexesPlacement[ind] = i

mat = {}
for el in indexesPlacement:
    x = indexesPlacement[el]
    toInt = int(el)
    temp = []
    for text in arrays:
        c = text[x]
        c = c.replace(' ', '')
        if c:
            temp.append(c)
    mat[toInt] = temp 

array = []
for text in rools:
    for chars in textToRemove:
        text = text.replace(chars, '')
    a, b, c = text.split()
    array.append((int(a), int(b), int(c)))

# PART ONE
for el in array:
    bouger, de, a = el
    index = bouger - 1
    if index == 0:
        item = mat[de].pop(0)
        mat[a].insert(0, item)
    else:
        for i in range(index + 1):
            item = mat[de].pop(0)
            mat[a].insert(0, item)

# PART TWO
# for el in array:
#     bouger, de, a = el
#     newArray = np.concatenate((mat[de][:bouger], mat[a]))
#     index = bouger
#     del mat[de][:index]
#     mat[a] = list(newArray)

code = []
for item in mat:
    c = mat[item][0]
    code.append(c)
textCode = ''.join(c for c in code)
print(textCode)

# EXAMPLE
"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""