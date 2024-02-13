def solution(arr):
    length = len(arr)
    # 배열의 길이가 2의 거듭제곱이 될 때까지 0을 추가해야 하는 개수 계산
    target_length = 1
    while target_length < length:
        target_length *= 2
    zeros_to_add = target_length - length
    # 0을 추가하여 반환
    return arr + [0] * zeros_to_add