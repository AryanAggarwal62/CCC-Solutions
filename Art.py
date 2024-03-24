numdots = int(input())
xmax = 0
ymax = 0
xmin = 100
ymin = 100
bottomleft = 0
topright = 0

for i in range(numdots):
    dotcoor = input()+'a'
    comma = dotcoor.find(',')
    x = dotcoor[0:comma]
    y = dotcoor[comma+1:-1]
    x = int(x)
    y = int(y)
    if x > xmax:
        xmax = x
    if y > ymax:
        ymax = y
    if x < xmin:
        xmin = x
    if y < ymin:
        ymin = y

bottomleft = str(xmin-1)+', '+str(ymin-1)
print(bottomleft)
topright = str(xmax+1)+', '+str(ymax+1)
print(topright)