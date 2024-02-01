def solution(myString, pat):
    modified_string = myString.replace("A", "X").replace("B", "A").replace("X", "B")
        # 변환된 문자열에서 pat을 찾습니다.
    if pat in modified_string:
        return 1
    else:
        return 0