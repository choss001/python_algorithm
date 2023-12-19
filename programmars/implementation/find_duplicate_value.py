def find_max_duplicate(arr):
    if not arr:
        return None

    # Create a dictionary to store counts of each element
    count_dict = {}
    
    # Iterate through the array and update counts in the dictionary
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Find the element with the maximum count (mode)
    max_duplicate = max(count_dict, key=count_dict.get)

    return max_duplicate

# Example usage:
my_array = [3, 7, 2, 7, 8, 7, 4, 3, 2, 7, 7]
max_duplicate_value = find_max_duplicate(my_array)

print(f"The maximum duplicate value is: {max_duplicate_value}")
