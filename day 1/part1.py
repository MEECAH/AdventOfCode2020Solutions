import sys

arr = []

with open(sys.argv[1]) as openfileobject:
    for line in openfileobject:
        line = line.replace("\n", "")
        integer = int(line, 10)
        arr.append(integer)
        
x = 0 
y = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        a = arr[i]
        b = arr[j]
        c = a + b
        if(c==2020):
            x = a
            y = b   
print(x*y)    
