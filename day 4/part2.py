import sys
import string

validPassports = 0
arr = []
haveAllFields = []
entry = ''
validCount = 0
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validFields = 0

byrLen = 4
minByr = 1920
maxByr = 2002+1 #+1 because the rule is upper bound inclusive and range() is exclusive on upper bounds

iyrLen = 4
minIyr = 2010
maxIyr = 2020+1

eyrLen = 4
minEyr = 2020
maxEyr = 2030+1 

minHgtCm = 150
maxHgtCm = 193+1

minHgtIn = 59
maxHgtIn = 76+1

hclLen = 7
allowedHclChars = string.ascii_lowercase[:6] + string.ascii_uppercase[:6] + string.digits + '#'

validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

pidChars = string.digits
pidLength = 9

with open(sys.argv[1]) as openfileobject:
    for line in openfileobject:
        line = line.strip()
        if line == '':
            arr.append(entry)
            arr.append(line)
            entry=''
        else:
            entry += (line+' ')
    arr.append(entry)

for i in range(len(arr)):
    if all(val in arr[i] for val in fields):
        haveAllFields.append(arr[i].split(' '))

for i in range(len(haveAllFields)):
     for j in range(len(haveAllFields[i])):

        field = haveAllFields[i][j].split(':')

        key = field[0]
        if key != '':
            val = field[1]

            if key == 'byr':
                if len(val) == byrLen and (int(val,10) in range(minByr,maxByr)):
                    validFields+=1
            elif key == 'iyr':
                if len(val) == iyrLen and (int(val,10) in range(minIyr,maxIyr)):
                    validFields+=1
            elif key == 'eyr':
                if len(val) == eyrLen and (int(val,10) in range(minEyr,maxEyr)):
                    validFields+=1
            elif key == 'hgt':
                if val[-2:] == 'cm':
                    val = int(val[:-2],10)
                    if val in range(minHgtCm,maxHgtCm):
                        validFields+=1
                elif val[-2:] == 'in':
                    val = int(val[:-2],10)
                    if val in range(minHgtIn,maxHgtIn):
                        validFields+=1
            elif key == 'hcl':
                if len(val) == hclLen:
                    if val[:1] == '#':
                        if all(c in allowedHclChars for c in val):
                            validFields+=1
            elif key == 'ecl':
                if val in validEyeColors:
                    validFields+=1
            elif key == 'pid':
                if all(c in pidChars for c in val):
                    if len(val) == pidLength:
                        validFields+=1

            elif key == 'cid':
                pass
        else:
            if(validFields>=7):
                validPassports+=1
            validFields=0

print(validPassports)