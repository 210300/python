n = int(input())
for i in range(n):
    expersion = input()
    if(expersion == "P=NP"):
        print("skipped")
    else:
        x, y = list(map(int, expersion.split("+")))
        print(x+y)