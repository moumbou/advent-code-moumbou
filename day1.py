file = open('info.txt', 'r')
info = file.readlines()
file.close()

totale = 0
calories = []
for line in info:
    text = line.replace('\n', '')
    if len(text):
        totale += int(text)
    else:
        if totale != 0:
            calories.append(totale)
        totale = 0
else:
    calories.append(totale)

# PART ONE
calories.sort(reverse=True)
print(calories[0])

sumCalories = 0
for i,_ in enumerate(range(3)):
    sumCalories += calories[i]

# PART TWO
print(sumCalories)

"""
EXAMPLE

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000

"""