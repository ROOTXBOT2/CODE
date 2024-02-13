def solution(arr1, arr2):
    # 두 배열의 길이를 비교
    if len(arr1) < len(arr2):
        return -1
    elif len(arr1) > len(arr2):
        return 1
    else:
        # 배열의 길이가 같을 경우, 각 배열의 합을 비교
        sum_arr1 = sum(arr1)
        sum_arr2 = sum(arr2)
        if sum_arr1 < sum_arr2:
            return -1
        elif sum_arr1 > sum_arr2:
            return 1
        else:
            return 0