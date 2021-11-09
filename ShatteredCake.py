width = int(input())
total = 0
for _ in range(int(input())):
    x, y = [int(x) for x in input().split()]    
    sum = x*y
    total = total+sum
print(int(total/width))


