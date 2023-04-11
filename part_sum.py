def solution(sequence, k):
    sdx, edx = 1, 1
    asdx, aedx = -1,-1
    ln = int(1e9)


    sequence = [0] + sequence
    prefix_sum = [0] * len(sequence)

    # prefix_sum 계산
    for i in range(1, len(sequence)):
        prefix_sum[i] = prefix_sum[i - 1] + sequence[i]

    # [0, 1, 3, 6, 10, 15]
    while sdx <= edx < len(sequence):
        check = prefix_sum[edx] - prefix_sum[sdx - 1]

        if check < k:
            edx += 1
        elif check == k:
            if ln > edx - sdx:
                ln = edx-sdx
                asdx, aedx = sdx, edx
            edx += 1
        else:
            sdx += 1


    return [asdx - 1, aedx - 1]
