longstring = input()
firsttext = input()
found = False
length = len(firsttext)

for i in range(length):
    firsttext = firsttext[1:]+ firsttext[0]
    if longstring.find(firsttext) >= 0:
        found = True
        break


if found:
    print('yes')
else:
    print('no')