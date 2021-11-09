n = int(input())
for _ in range(n):
    x = [int(y) for y in input().split()[:-1]]
    total = 0
    for l, h in zip(x,x[1:]):
        if(l*2)<h:
            total+=h-l*2
    print(total)