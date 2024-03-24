'''
def get_dist(coords):
    all_dist = []
    all_dist.append(yard-int(coords[0])) # dist down
    all_dist.append(int(coords[0])-1) #dist up
    all_dist.append(yard-int(coords[1])) #dist right
    all_dist.append(int(coords[1])-1) #dist left
    
    closest_fence = min(all_dist)
    
    if all_dist.count(closest_fence)>1:
        if all_dist.find(closest_fence) == 0
    
    if all_dist.find(closest_fence) == 0:
        closest_bottom.append(closest_fence)
    elif all_dist.find(closest_fence) == 1:
        closest_top.append(closest_fence)
    elif all_dist.find(closest_fence) == 2:
        closest_right.append(closest_fence)
    else:
        closest_left.append(closest_fence)
'''     
    

yard = int(input())
num_t = int(input())
trees = []

closest_bottom = [0]
closest_top = [0]
closest_right = [0]
closest_left = [0]

for i in range(num_t):
    trees.append(input().split(" "))

for i in trees:
    all_dist = []
    
    all_dist.append(yard-int(i[0])) # dist down
    all_dist.append(int(i[0])-1) #dist up
    all_dist.append(yard-int(i[1])) #dist right
    all_dist.append(int(i[1])-1) #dist left
    
    closest_fence = min(all_dist)
    '''
    if all_dist.count(closest_fence)>1:
        if all_dist.find(closest_fence) == 0
    '''
    '''
    if all_dist.count(closest_fence) > 1:
        if count == 4:
            closest
    '''
    
    if all_dist.index(closest_fence) == 0:
        closest_bottom.append(closest_fence)
    elif all_dist.index(closest_fence) == 1:
        closest_top.append(closest_fence)
    if all_dist.index(closest_fence) == 2:
        closest_right.append(closest_fence)
    else:
        closest_left.append(closest_fence)

height = yard-(max(closest_top)+max(closest_bottom))
width = yard-(max(closest_left)+max(closest_right))

print(min(height,width))
    
    

#look at shortest side for each tree
