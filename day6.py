file = open('info.txt', 'r')
info = file.readlines()
file.close()

message = info[0]

# FIRST PART
# for i,c in enumerate(message):
#     end = i + 4
#     carachters = message[i:end]
#     repeated = {i:carachters.count(i) for i in carachters}
#     if len(repeated) > 3:
#         print(end)
#         break

# SECOND PART
for i,c in enumerate(message):
    end = i + 14
    carachters = message[i:end]
    repeated = {i:carachters.count(i) for i in carachters}
    if len(repeated) > 13:
        print(end)
        break

"""
EXAMPLE

bvwbjplbgvbhsrlpgdmjqwftvncz

"""