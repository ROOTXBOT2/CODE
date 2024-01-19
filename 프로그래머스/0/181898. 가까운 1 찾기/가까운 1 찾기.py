def solution(arr, idx):
    answer = 0
    return [i for i in range(idx, len(arr)) if arr[i] == 1][0] if [i for i in range(idx, len(arr)) if arr[i] == 1] else -1
