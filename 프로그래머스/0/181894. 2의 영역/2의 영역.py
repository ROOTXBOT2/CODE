def solution(arr):
    # 배열에 2가 있는지 확인
    if 2 not in arr:
        return [-1]

    # 2가 포함된 모든 인덱스 찾기
    indexes = [i for i, x in enumerate(arr) if x == 2]

    # 2가 포함된 가장 작은 연속된 부분 배열 찾기
    start = min(indexes)
    end = max(indexes)

    # 부분 배열 반환
    return arr[start:end+1]
