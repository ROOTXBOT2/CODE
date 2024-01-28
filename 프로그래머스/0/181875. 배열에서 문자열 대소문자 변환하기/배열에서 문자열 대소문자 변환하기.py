def solution(strArr):
    answer = [strArr[i].lower() if i % 2 == 0 else strArr[i].upper() for i in range(len(strArr))]
    return answer