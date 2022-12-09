file = open('info.txt', 'r')
info = file.readlines()
file.close()

commands = []
for text in info:
    text = text.replace('\n', '')
    if len(text):
        commands.append(text)

def getPath(text, path):
    splitedText = text.split()
    if splitedText[1] == 'cd':
        if splitedText[2] != '..':
            path.append(splitedText[2])
        else:
            lastIndex = len(path) - 1
            path.pop(lastIndex)
path = []
folders = {}
for c in commands:
    getPath(c, path)
    directory = '-'.join(char for char in path)
    splitedText = c.split()
    if splitedText[0] == '$':
        if splitedText[1] == 'ls':
            folders[directory] = {'content': [], 'size': 0}
            
    if splitedText[0] == 'dir':
        content = directory + '-' + splitedText[1]
        folders[directory]['content'].append(content)
    
    if splitedText[0] != 'dir' and splitedText[0] != '$':
        folders[directory]['size'] += int(splitedText[0])

isNested = True
while isNested:
    isNested = False
    for directory in folders:
        content = folders[directory]['content']
        if len(content):
            isNested = True
            for i,c in enumerate(content):
                contentX = folders[c]['content']
                if len(contentX) == 0:
                    folders[directory]['size'] += folders[c]['size']
                    folders[directory]['content'].pop(i)

# PART ONE
# sumSizes = 0
# for f in folders:
#     if f != '/':
#         if folders[f]['size'] <= 100_000:
#             sumSizes += folders[f]['size']

# PART TWO
sizes = []
for f in folders:
    if folders[f]['size'] >= 8381165:
        sizes.append(folders[f]['size'])

sizes.sort()
print(sizes[0])

"""

!PS: this is not a real solution for the problem WELL I TRIED !

Example:

$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k

"""