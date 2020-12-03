import sys
from itertools import cycle

arr = []

with open(sys.argv[1]) as openfileobject:
    for line in openfileobject:
        line = line.replace("\n", "")
        arr.append(line)

        
trees = 0
empties = 0

rightMoves = int(sys.argv[2],10)
downMoves = int(sys.argv[3],10)

nums = list(range(0, len(arr[0])))

numCycle = cycle(nums)
numCycle.next()

for i in range(1,len(arr)):
    for k in range(0,rightMoves-1):
        numCycle.next()
    loc = arr[i][numCycle.next()]
    if loc == "#":
        trees+=1
    else:
        empties+=1

print(trees)

    
