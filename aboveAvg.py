c = int(input())
for _ in range(c):
    N, *grades = tuple(map(int, input().split()))
    mean = sum(grades) / N
    above = 0
    for grade in grades:
        if grade > mean:
            above += 1
    print("%.3f%s" % (round(above / N * 100, 3), '%'))