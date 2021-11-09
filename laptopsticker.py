wc, hc, ws, hs= list(map(int, input().split()))
if wc-ws <2:
    print(0)
    exit()
elif hc - hs <2:
    print(0)
    exit()
print(1)