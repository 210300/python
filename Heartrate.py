for _ in range(int((input()))):
    r, c = [float(x) for x in input().split()]
    k = 60.0
    ans = round(k*(r/c),4)
    var = round((k/c),4)
    x = round((ans+var),4)
    y = round((ans-var),4)
    print(y,ans,x)
