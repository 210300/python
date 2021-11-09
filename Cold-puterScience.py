def main():
    x = int(input())
    y = list(map(float,input().split()))
    count = 0
    for t in y:
        if(t<0):
            count+=1
    print(count)
if __name__ == '__main__':
    main()