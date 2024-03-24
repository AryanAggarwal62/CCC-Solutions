days = int(input())
daylist = []
availabilitylist = []
highestlist = []
count=0
counter = 0
newlist = []
daycount = 0

for i in range(days):
    availability = input()
    day1 = availability[0]
    day2 = availability[1]
    day3 = availability[2]
    day4 = availability[3]
    day5 = availability[4]
    daylist.append(day1)
    daylist.append(day2)
    daylist.append(day3)
    daylist.append(day4)
    daylist.append(day5)

#add first number to list, remove it from previous list
for i in range(5):
    day1list = daylist[::5]
    day1list = ''.join(day1list)
availabilitylist.append(day1list)

for i in range(5):
    day2list = daylist[1::5]
    day2list = ''.join(day2list)
availabilitylist.append(day2list)

for i in range(5):
    day3list = daylist[2::5]
    day3list = ''.join(day3list)
availabilitylist.append(day3list)

for i in range(5):
    day4list = daylist[3::5]
    day4list = ''.join(day4list)
availabilitylist.append(day4list)

for i in range(5):
    day5list = daylist[4::5]
    day5list = ''.join(day5list)
availabilitylist.append(day5list)



for i in range(5):
    count = availabilitylist[i]
    a=count.count('Y')
    highestlist.append(a)

maxhighest = max(highestlist)
amountofhighest = highestlist.count(maxhighest)


    
    

if amountofhighest == 1:
    highestlistindex = highestlist.index(maxhighest)
    if highestlistindex == 0:
        print(1)
    elif highestlistindex == 1:
        print(2)
    elif highestlistindex == 2:
        print(3)
    elif highestlistindex == 3:
        print(4)
    elif highestlistindex == 4:
        print(5)
elif amountofhighest > 1:
    for i in range(amountofhighest):
        highestlistindex = highestlist.index(maxhighest)
        if i == 0:
            if highestlistindex == 0:
                print('1,',end='')
            elif highestlistindex == 1:
                print('2,',end='')
            elif highestlistindex == 2:
                print('3,',end='')
            elif highestlistindex == 3:
                print('4,',end='')
            elif highestlistindex == 4:
                print('5,',end='')
        elif i > 0:
            if len(str(highestlist)) > 1:
                if highestlistindex == 0:
                    print(1+i,',',end='',sep='')
                elif highestlistindex == 1:
                    print(2+i,',',end='',sep='')
                elif highestlistindex == 2:
                    print(3+i,',',end='',sep='')
                elif highestlistindex == 3:
                    print(4+i,',',end='',sep='')
                elif highestlistindex == 4:
                    print(5+i,',',end='',sep='')
                highestlist.remove(maxhighest)
                
            elif len(str(highestlist)) == 1:
                if highestlistindex == 0:
                    print(1+i,',',end='',sep='')
                elif highestlistindex == 1:
                    print(2+i,',',end='',sep='')
                elif highestlistindex == 2:
                    print(3+i,',',end='',sep='')
                elif highestlistindex == 3:
                    print(4+i,',',end='',sep='')
                elif highestlistindex == 4:
                    print(5+i,',',end='',sep='')
                highestlist.remove(maxhighest)
               
    
    





    
    
    
    
    



