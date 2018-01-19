import re

# rotate right
def rotate90(pattern):
    temppattern=[]
    for x in range(0,len(pattern)):
        temprow=""
        for y in range(0,len(pattern)):
            temprow=temprow+(pattern[y][x])
        temppattern.append(temprow[::-1])
    return temppattern
# rotate right twice
def rotate180(pattern):
    temppattern=pattern
    for x in range(0,2):
        temppattern=rotate90(temppattern)
    return temppattern
# rotate right 3
def rotate270(pattern):
    temppattern=pattern
    for x in range(0,3):
        temppattern=rotate90(temppattern)
    return temppattern
# flip
def flipit(pattern):
    temppattern=[]
    for x in reversed(pattern):
        temppattern.append(x)
    return temppattern
# flip-rotate right
def flipNrotate90(pattern):
    temppattern=flipit(pattern)
    temppattern=rotate90(temppattern)
    return temppattern
# flip-rotate right twice
def flipNrotate180(pattern):
    temppattern=flipit(pattern)
    for x in range(0,2):
        temppattern=rotate90(temppattern)
    return temppattern
# flip-rotate left
def flipNrotate270(pattern):
    temppattern=flipit(pattern)
    for x in range(0,3):
        temppattern=rotate90(temppattern)
    return temppattern

def doesitmatch(pattern,inputPattern):
    if pattern==inputPattern:
        return True
    elif pattern==rotate90(inputPattern):
        return True
    elif pattern==rotate180(inputPattern):
        return True
    elif pattern==rotate270(inputPattern):
        return True
    elif pattern==flipit(inputPattern):
        return True
    elif pattern==flipNrotate90(inputPattern):
        return True
    elif pattern==flipNrotate180(inputPattern):
        return True
    elif pattern==flipNrotate270(inputPattern):
        return True
    else:
        return False


def breakitup(pattern,therules):

    if len(pattern[0])%2==0:
        size=int(len(pattern[0]))
        newpattern=[]
        thepattern=[]
        for x in range(0, size, 2):
            print("clear pattern")
            partpattern=[]
            for y in range(0, size, 2):
                partpattern=([pattern[x][y]+pattern[x][y+1],pattern[x+1][y]+pattern[x+1][y+1]])
                print(partpattern)
                for i in range(0,len(therules)):
                    if (doesitmatch(partpattern,therules[i][0])):
                        print(therules[i][1])
                        newpattern.append(therules[i][1])
            print(newpattern)





thefile  = open("input.txt", "r")
thedata= thefile.read()
thedata=re.split(r'\n+', thedata)
therules = thedata[:-1]

for x in range(0,len(therules)):
    therules[x]=therules[x].strip().strip().split("=>")
    for y in range(0,len(therules[x])):
        therules[x][y]=therules[x][y].strip().strip().split("/")

pattern=[".#.","..#","###"]
# pattern=["###.#.#.#","#...#.#.#","#.###.#.#",".#.##.#.#",".#.##.#.#",".#..#.#.#","##.##.#.#",".####.#.#",".#..#.#.#"]


# for l in range(0,len(pattern)):
#     print(pattern[x])
# print()
for i in range(5):
    for l in range(0,len(pattern)):
        print(pattern[l])
    print()
    pattern=breakitup(pattern,therules)



thesum=0
for row in pattern:
    thesum=row.count("#")+thesum
print(thesum)
