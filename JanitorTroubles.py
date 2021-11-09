import math
def maxarea(a,b,c,d):
    x = (a+b+c+d) / 2
    return math.sqrt((x-a)*(x-b)*(x-c)*(x-d))

a,b,c,d = [int(x) for x in input().split()]
print(maxarea(a, b, c, d))