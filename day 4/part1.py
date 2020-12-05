import sys

arr = []
string = ''
validCount = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open(sys.argv[1]) as openfileobject:
    for line in openfileobject:
        line = line.strip()
        if line == '':
            arr.append(string)
            arr.append(line)
            string=''
        else:
            string += (line+' ')
    arr.append(string)
        
# for i in range(len(arr)):
#     if all(map(arr[i].__contains__, fields)):
#         validCount+=1

for i in range(len(arr)):
    if all(val in arr[i] for val in fields):
        validCount+=1

print(validCount)
