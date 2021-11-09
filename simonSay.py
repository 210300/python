n = int(input())
for _ in range(n):
    line = input()
    if line.startswith("Simon says"):
        print(line[10:])
    else:
        print()

