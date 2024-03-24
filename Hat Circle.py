def count_matching_hats(n, hat_numbers):
    count = 0
    # Check the first half of the people
    for i in range(n // 2):
        # Index of person directly across
        across_index = (i + n // 2) % n
        # Check if hats match
        if hat_numbers[i] == hat_numbers[across_index]:
            count += 2 # Increment by 2 (both hats see each other)
    return count


# number of people
n = int(input())
    
# hat numbers list
hat_numbers = []
    
# add hat numbers to list
for i in range(n):
    hat_numbers.append(int(input()))
    
matching_hats = count_matching_hats(n, hat_numbers)
print(matching_hats)