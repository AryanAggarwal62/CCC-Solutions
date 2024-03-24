lines = int(input())

for i in range(lines):
    code = input()
    space = code.find(' ')
    number = code[0:space]
    symbol = code[space:]
    number = int(number)
    print(symbol*number)
    