books_current  = list(input())
num_b = len(books_current)-1
index = 0
count = 0

books_sorted = list("L" * books_current.count("L")) + list("M" * books_current.count("M")) + list("S"* books_current.count("S"))

while books_current != books_sorted:
    if books_current[index] != books_sorted[index]:
        last_occ = "".join(books_current).rfind(books_sorted[index])
        books_current[last_occ], books_current[index] = books_current[index], books_current[last_occ]
        
        count += 1
        
    index += 1

print(count)
    