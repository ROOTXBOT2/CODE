def solution(arr, flag):
    X = []  # 빈 배열 X 초기화
    for i in range(len(arr)):
        if flag[i]:  # flag[i]가 True인 경우
            X.extend([arr[i]] * (arr[i] * 2))  # arr[i]를 arr[i] * 2번 X에 추가
        else:  # flag[i]가 False인 경우
            X = X[:-arr[i]]  # X에서 마지막 arr[i]개의 원소를 제거
    return X