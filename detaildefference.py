def test():
    text1 = input()
    text2 = input()
    defference = ""
    for letter1,letter2 in zip(text1,text2):
        if letter1 == letter2:
            defference +='.'
        else:
            defference +="*"
    print(text1)
    print(text2)
    print(defference)
    print("")
n = int(input())
for _ in range(n):
    test()