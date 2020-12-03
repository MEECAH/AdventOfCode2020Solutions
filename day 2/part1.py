import sys

arr = []
validCount = 0

with open(sys.argv[1]) as openfileobject:
    for line in openfileobject:
        line = line.replace("\n", "")
        arr.append(line)
        

for i in range(len(arr)):
     line = arr[i]
     line = line.replace(" ", "")
     split = line.split(':')
     rule = split[0]
     password = split[1]
     ruleChar = rule[len(rule)-1]
     rule = rule.replace(ruleChar, "")
     bounds = rule.split('-')
     lb = int(bounds[0], 10)
     hb = int(bounds[1], 10)
     occurs = password.count(ruleChar)
     if(lb<=occurs and occurs<=hb):
         validCount+=1

print(validCount)