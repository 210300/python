number = int(input('Enter number: '))
copy = number
digit_sum = 0
while True:
    digit_sum += number%10
    number //= 10
    if copy%digit_sum == 0:
        print(copy)
        break
    else:
        number += 1
        print(number)