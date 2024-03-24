'''
tune = input()
tune = tune+'a'
plus = (tune.find('+'))
minus = (tune.find('-'))
pluscount = (tune.count('+'))
minuscount = (tune.count('-'))
plusandminus = pluscount + minuscount
replacedtune = []



newtune = tune.replace('+',' tighten ')
newtune = newtune.replace('-',' loosen ')
for i in range(plusandminus):
    nindex = newtune.find('n')
    newnindex = nindex+3
    replacedtune = newtune[0:newnindex]
    print(replacedtune)
    newtune = newtune[newnindex:-1]
    
'''
tone = input()+" "
prev_index = 0

for i in range(len(tone)):
    if "0123456789".find(tone[i]) != -1: #checks if num
        if "0123456789".find(tone[i+1]) == -1: #checks if str after num
            command = tone[prev_index:i+1]
            if command.find("+") != -1: #check and replace + or -
                print(command.replace("+", " tighten "))

            else:
                print(command.replace("-", " loosen "))
            prev_index = i+1 # changes the starting index of next adjustment