def solution(want, number, discount):
    dic_wishlist = {}
    answer = 0
    for i in range(len(want)):
        dic_wishlist[want[i]] = number[i]
    print(f'dic_wishlist={dic_wishlist}')
    for i in range(len(discount) - 9):
        dic_temp = dic_wishlist.copy()
        for j in range(i,i+10):
            if discount[j] in dic_temp and dic_temp[discount[j]] != 0:
                dic_temp[discount[j]] -= 1
            else:
                break
        if sum(dic_temp.values()) == 0:
            answer += 1
    return answer

want, number, discount = ["banana", "apple", "rice", "pork", "pot"],\
[3, 2, 2, 2, 1],\
["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))

