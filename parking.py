n  = int(input())
for _ in  range(n):
    d = int(input())
    f = list(map(lambda location: int(location),input().split()))
    last = max(f)
    frist = min(f)
    answer = 2 * (last-frist)
    print(answer)
    