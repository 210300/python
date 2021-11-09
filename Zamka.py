def find_its_digits(num):
    return sum([int(x) for x in str(num)])
L = int(input())
D = int(input())
X = int(input())

M = 0
N = 0

for i in range(L,D+1):
    if(find_its_digits(i) == X):
        M = i
        break
for i in range(D,L-1,-1):
    if(find_its_digits(i) == X):
        N = i
        break
print(M)
print(N)