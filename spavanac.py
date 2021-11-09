hour, minu = [int(x) for x in input().split()]
if minu-45<0:
    hour-=1
    if(hour<0):
        hour=23
    minu = 60-abs(minu-45)
else:
    minu = minu -45
print(hour, minu)