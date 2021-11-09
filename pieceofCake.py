n,h,v = [int(x) for x in input().split()]
volumn = max(v,n-v)*max(h,n-h)*4
print(volumn)