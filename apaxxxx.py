last =""
out = ""
for i in input().strip():
    if(last != i):
        out+=i
    last = i
print(out)