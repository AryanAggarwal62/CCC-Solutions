nbids = int(input())
max_bid = 0
max_name = ''

for i in range(nbids):
    name = input()
    bid = int(input())
    if bid > max_bid:
        max_bid = bid
        max_name = name
print(max_name)