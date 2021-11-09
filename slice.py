import math
n,w,h = [int(x) for x in input().split()]
y = math.sqrt(w*w+h*h)+0.01
for _ in range(n):
    if(int(input())<y):
        print("DA")
    else:
        print("NE")


