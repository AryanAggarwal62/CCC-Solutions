def solution(crypt, solution):
    # Create a dictionary to store the mapping between letters and digits
    mapping = {}
    for s in solution:
        mapping[s[0]] = s[1]
    
    # Check if any of the words have leading zeros
    if any(len(word) > 1 and mapping[word[0]] == '0' for word in crypt):
        return False
    
    # Convert the words in crypt to their corresponding digit strings
    nums = []
    for word in crypt:
        num = ''.join(mapping[c] for c in word)
        nums.append(num)
    
    # Check if the sum of the first two numbers equals the third number
    return int(nums[0]) + int(nums[1]) == int(nums[2])

