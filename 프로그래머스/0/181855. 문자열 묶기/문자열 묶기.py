def solution(strArr):
    # 각 문자열의 길이를 세어서 딕셔너리에 저장
    length_count = {}
    for string in strArr:
        length = len(string)
        if length not in length_count:
            length_count[length] = 0
        length_count[length] += 1

    # 가장 많이 등장한 문자열 길이를 찾음
    max_count = 0
    for count in length_count.values():
        max_count = max(max_count, count)

    return max_count