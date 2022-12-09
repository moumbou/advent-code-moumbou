file = open('info.txt', 'r')
info = file.readlines()
file.close()

list = []
for i in info:
    text = i.replace('\n', '')
    list.append(text)

finalList = []
# FIRST PART
# for i in list:
#     complet = len(i)
#     half = int(len(i) / 2)
#     a = i[0:int(half)]
#     b = i[half:complet]
#     finalList.append((a, b))

# listChars = []
# for t in finalList:
#     a, b = t
#     for c in a:
#         if c in b:
#             listChars.append(c)
#             break

for i, text in enumerate(list):
    result = i + 1
    if result % 3 == 0:
        a = list[i]
        b = list[i - 1]
        c = list[i - 2]
        finalList.append((a,b,c))


listChars = []
for t in finalList:
    x, y, z = t
    for c in x:
        if c in y and c in z:
            listChars.append(c)
            break

counter = 0
for c in listChars:
    result = ord(c) - 96
    if result > 0:
        counter += result
    else:
        result = ord(c.lower()) - 96
        result += 26
        counter += result

print(counter)

"""
EXAMPLE

WVHGHwddqSsNjsjwqVvdwZRCbcJcZTCcsZbLcJJsCZ
hngprFFhFDFhrDpzzQDhtnBJJRJZbZvTcvbfRCJfBRcBJl
DmptngtFwvvMmwmm
HFddrJnLdqtHBMQBmmVm
gbvNsbhsvQtmZTbQPT
vDshDlczcDhcssscwzQwslLJrSJLpqrrzpnCrSfLSnqq
pDGQDSpFDGzFDQSJqzDhjhQMTjTrwTstbTBTjTtLtbTMBT
zgzVNHHgMwMLbLNB
WRWPgdHCZccggJmJGzJmzGhGCD

"""
