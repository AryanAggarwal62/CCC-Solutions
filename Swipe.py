n = int(input())
array_a = [int(i) for i in input().split()]
array_b = [int(i) for i in input().split()]

if array_a == array_b:
    print('YES')
    print('0')
else:
    if array_a[1] != array_b[1] and array_b.count(array_a[0]) == 2:
        print("YES")
        print("1")
        print("R 0 1")
    elif array_a[0] != array_b[0] and array_b.count(array_a[1]) == 2:
        print("YES")
        print(1)
        print("L 0 1")
    else:
        print('NO')
