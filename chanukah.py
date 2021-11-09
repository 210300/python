for _ in range(int(input())):
    p,n = [int(x) for x in input().split()]
    answer = int(n*(n+1)/2+n)
    print(p, answer)
