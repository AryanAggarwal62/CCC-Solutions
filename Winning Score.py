a3 = int(input())
a2 = int(input())
a1 = int(input())
atotal = a3*3 + a2*2 + a1
b3 = int(input())
b2 = int(input())
b1 = int(input())
btotal = b3*3 + b2*2 + b1

total = atotal-btotal

if total > 0:
    print('A')
elif total < 0:
    print('B')
elif total == 0:
    print('T')