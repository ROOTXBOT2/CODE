def solution(a, d, included):
    answer = 0
    for i, boolean in enumerate(included):
        if boolean:
            answer = answer + (a + d*i)
    return answer

