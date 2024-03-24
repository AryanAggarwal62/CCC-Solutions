totalplayers = int(input())
goldcount = 0

for i in range(totalplayers):
    points = int(input())
    fouls = int(input())
    points = points*5
    fouls = fouls*3
    totalpoints = points - fouls
    if totalpoints > 40:
        goldcount = goldcount + 1

if goldcount == totalplayers:
    gold = "+"
else:
    gold = ""

print(goldcount,gold,sep='')
        