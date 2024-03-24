sensors = int(input())
readings = []
frequency = []
count = 0
run = True
counter = 0
absolutevalue = 0
xcount = 0

for i in range(sensors):
    reading = int(input())
    readings.append(reading)
ogreadings = readings



for i in readings:
    a = readings.count(i)
    frequency.append(a)
    
while run:
    for i in range(len(frequency)-1):
        if frequency[i] != 'a':
            if frequency[i] == frequency[i+1]:
                if readings[i] == readings[i+1]:
                    del frequency[i+1]
                    frequency.append('a')
                    counter += 1
                    del readings[i+1]
                    readings.append('a')
                else:
                    xcount += 1
                    if xcount == sensors:
                        run = False
            else:
                count += 1
                if count == sensors:
                    run = False
                
for i in range(counter):
    frequency.remove('a')
    readings.remove('a')
simplereadings = readings
simplefrequency = frequency
#print('all numbers, once',simplereadings)


mostfrequent = max(frequency) # 2
numoflargest = frequency.count(mostfrequent)
largestlist = []
largestnumbers = []

for i in range(numoflargest):
    indexhighestsensor = frequency.index(mostfrequent) 
    highestsensor = frequency[indexhighestsensor]     
    largestlist.append(highestsensor)
    frequency.remove(highestsensor)
    highestsensor = readings[indexhighestsensor]
    largestnumbers.append(highestsensor)
    readings.remove(highestsensor)
   
    
#print('largest list is:',largestlist)
#print('largest numbers is:',largestnumbers)

if len(largestnumbers) == 2:
    num1 = largestnumbers[0]
    num2 = largestnumbers[1]
    absolutevalue = abs(num1-num2)
elif len(largestnumbers) > 2:
    num1 = largestnumbers[0]
    mostfrequent = max(frequency) # 2
    numoflargest = frequency.count(mostfrequent)
    largestlist = []
    largestnumbers = []

    for i in range(numoflargest):
        indexhighestsensor = frequency.index(mostfrequent) 
        highestsensor = frequency[indexhighestsensor]     
        largestlist.append(highestsensor)
        frequency.remove(highestsensor)
        highestsensor = readings[indexhighestsensor]
        largestnumbers.append(highestsensor)
        readings.remove(highestsensor)
    
    
    for i in range(len(largestnumbers)):
        value = abs(largestnumbers[i]-num1)
        if value > absolutevalue:
            absolutevalue = value
elif len(largestnumbers) < 2:
        for j in range(len(ogreadings)):
            value = abs(largestnumbers[0]-ogreadings[j])
            if value > absolutevalue:
                absolutevalue = value
    
print(absolutevalue)
