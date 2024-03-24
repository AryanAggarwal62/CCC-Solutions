numpeppers = int(input())
spicy = 0

for i in range(numpeppers):
    pepper = input()
    if pepper == 'Poblano':
        spicy = spicy + 1500
    elif pepper == 'Mirasol':
        spicy = spicy + 6000
    elif pepper == 'Serrano':
        spicy = spicy + 15500
    elif pepper == 'Cayenne':
        spicy = spicy + 40000
    elif pepper == 'Thai':
        spicy = spicy + 75000
    elif pepper == 'Habanero':
        spicy = spicy + 125000
print(spicy)