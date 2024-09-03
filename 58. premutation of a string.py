def get_permutations(s):
    # Base case: If the string is empty, return an empty list
    if len(s) == 0:
        return []
    
    # Base case: If the string has one character, return a list with that single character
    if len(s) == 1:
        return [s]
    
    # List to store all permutations
    permutations = []
    
    # Iterate over the string
    for i in range(len(s)):
        # Fix one character and get all permutations of the remaining string
        char = s[i]
        remaining_string = s[:i] + s[i+1:]
        
        # Recursively get the permutations of the remaining string
        for p in get_permutations(remaining_string):
            # Add the fixed character to the front of each permutation
            permutations.append(char + p)
    
    return permutations

# Example usage:
s = "abc"
perms = get_permutations(s)
print(perms)
