import sys
from itertools import cycle

arr = []

with open(sys.argv[1]) as openfileobject:
    for line in openfileobject:
        line = line.replace("\n", "")
        arr.append(line)

def treesHit(right, down):

    trees = 0
    empties = 0

    rightMoves = right
    downMoves = down

    nums = list(range(0, len(arr[0])))

    numCycle = cycle(nums)
    numCycle.next()

    for i in range(downMoves,len(arr),downMoves):
        for k in range(0,rightMoves-1):
            numCycle.next()
        loc = arr[i][numCycle.next()]
        if loc == "#":
            trees+=1
        else:
            empties+=1

    return trees

result = treesHit(1,1)*treesHit(3,1)*treesHit(5,1)*treesHit(7,1)*treesHit(1,2)    
print(result)
