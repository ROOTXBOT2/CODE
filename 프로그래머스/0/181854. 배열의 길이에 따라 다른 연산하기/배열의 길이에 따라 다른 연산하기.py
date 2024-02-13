def solution(arr, n):
    result = []
    for i in range(len(arr)):
        # 홀수 길이의 배열이면서 홀수 인덱스인 경우
        if len(arr) % 2 == 1 and i % 2 == 0:
            result.append(arr[i] + n)
        # 짝수 길이의 배열이면서 짝수 인덱스인 경우
        elif len(arr) % 2 == 0 and i % 2 == 1:
            result.append(arr[i] + n)
        else:
            result.append(arr[i])
    return result