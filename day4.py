file = open('info.txt', 'r')
info = file.readlines()
file.close()

# FIRST PART
# pairs = 0
# for i in info:
#     text = i.replace('\n', '')
#     a, b = text.split(',')
#     x,y = a.split('-')
#     z,v = b.split('-')
#     x = int(x)
#     y = int(y) + 1
#     z = int(z)
#     v = int(v) + 1
#     ranx = [i for i in range(x,y)]
#     rany = [i for i in range(z,v)]
#     check = False
#     if len(ranx) > len(rany):
#         check = all(item in ranx for item in rany)
#     else:
#         check = all(item in rany for item in ranx)
#     if check:
#         pairs += 1

# SECOND PART
pairs = 0
checked = False
for i in info:
    text = i.replace('\n', '')
    a, b = text.split(',')
    x,y = a.split('-')
    z,v = b.split('-')
    x = int(x)
    y = int(y) + 1
    z = int(z)
    v = int(v) + 1
    ranx = [i for i in range(x,y)]
    rany = [i for i in range(z,v)]
    if x in rany and checked == False:
        pairs += 1
        checked = True
    if z in ranx and checked == False:
        pairs += 1
    checked = False

print(pairs)

"""
Example

4-90,1-4
80-94,80-81
1-97,96-99
20-87,20-88
84-84,83-88
9-75,10-75
7-25,24-48
10-99,11-98
4-98,1-1
20-42,1-42
5-31,6-31
9-14,15-84
87-98,22-81
44-69,45-68
2-2,2-83

"""
