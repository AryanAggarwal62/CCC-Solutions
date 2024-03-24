totalpeople = int(input())
day0 = int(input())
infected = int(input())
day = 0
final = day0
a=day0

while a <= totalpeople:
    final = final*infected
    a = a+final
    day += 1
print(day)
    