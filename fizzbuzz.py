x,y,n =[int(n) for n  in input().split()]
for i in range(1,1+n):
    if(i % x == 0 and i%y == 0):
        print('FizzBuzz')
    elif(i%x == 0):
        print('Fizz')
    elif(i%y == 0):
        print('Buzz')
    else:
        print(i)