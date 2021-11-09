totalNumber = int(input())
lastans = input()
noOfCorrectAns = 0
for _ in range(totalNumber-1):
    currentans = input()
    if lastans == currentans:
        noOfCorrectAns += 1
    lastans = currentans
print(noOfCorrectAns)
