def solution(want, number, discount):
    answer = 0
    dict_wishlist = {}

    for i in range(len(want)):
        dict_wishlist[want[i]] = number[i]
    print(f'dict_wishlist = {dict_wishlist}')
    for i in range(len(discount) - 9):
        print(f'i={i}')
        dict_tmp = dict_wishlist.copy()
        print(f'dict_tmp = {dict_tmp}')
        for j in range(i, i + 10):
            print(f'discount[{j}] = {discount[j]}')
            if discount[j] in dict_tmp and dict_tmp[discount[j]] != 0:
                dict_tmp[discount[j]] -= 1
                print(f'dict_tmp[{discount[j]}] -= 1')
            else:
                break
        if sum(dict_tmp.values()) == 0:
            answer += 1

    return answer

want, number, discount = ["banana", "apple", "rice", "pork", "pot"],\
[3, 2, 2, 2, 1],\
["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))

