def solution(myString, pat):
    # 문자열을 모두 소문자로 변환하여 비교
    myString = myString.lower()
    pat = pat.lower()
    
    # myString에서 pat을 찾음
    if pat in myString:
        return 1
    else:
        return 0