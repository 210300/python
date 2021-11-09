c = float(input())
l =  int(input())
total = 0
for _ in range(l):
    w1,l1 = [float(x) for x in input().split()]
    total += w1*l1*c
print(total)