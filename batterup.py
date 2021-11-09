n = int(input())
x = [int(x) for x in input().split() if(x!="-1")]
print(sum(x)/len(x))