def permutations(arr, size):
    if size == 0:
        return [[]]  # base case: an empty list has only one permutation, an empty list itself

    result = []  # to store the permutations

    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]  # remaining elements after excluding arr[i]
        sub_permutations = permutations(rest, size - 1)  # recursive call with reduced size

        for perm in sub_permutations:
            result.append([arr[i]] + perm)  # add arr[i] to each permutation of the remaining elements

    return result

# Example usage
my_list = [1, 2, 3, 4]
permutations_list = permutations(my_list, 2)
print(permutations_list)

