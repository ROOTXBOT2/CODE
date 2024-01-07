def solution(a, b):
    answer = str(b) + str(a)
    if str(a) + str(b) >= str(b) + str(a):
        answer = str(a) + str(b)
    return int(answer)