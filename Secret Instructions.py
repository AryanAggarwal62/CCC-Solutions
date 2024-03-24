end = True
num = 0
while end:
    num = int(input())
    firstnum = int(num/10000)
    secondnum = int(num/1000)
    secondnum -= firstnum*10
    sum = firstnum+secondnum
    steps = num%1000
    if num == 99999:
        end = False
    elif sum%2 == 0 and sum != 0:
        print("right",steps)
        previous = "right"
    elif sum%2 == 1:
        print("left",steps)
        previous = "left"
    elif sum == 0:
        print(previous,steps)