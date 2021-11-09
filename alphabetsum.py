chars = [ord(x) for x in input().strip()]
total = len(chars)
upper = len([x for x in chars if 64 < x < 91])
lower = len([x for x in chars if 96 < x < 123])
whitespace = chars.count(95)
symbol = total - upper - lower - whitespace
print(whitespace/total)
print(lower/total)
print(upper/total)
print(symbol/total)