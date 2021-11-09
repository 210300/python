def fact(x):
    if x == 0:
        return 1
    else:
        return x * fact(x-1)
for _ in range(int(input())):
    x = int(input())
    lastdigit = fact(x)%10
    print(lastdigit)
