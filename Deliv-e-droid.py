score = 0
packages = int(input())
collisions = int(input())
scorep = packages*50
scorec = collisions*10
if packages > collisions:
    score = 500
score = score + scorep - scorec
print(score)
