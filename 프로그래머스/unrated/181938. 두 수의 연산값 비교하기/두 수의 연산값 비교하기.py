def solution(a, b):
    answer = str(a) + str(b)
    if int(answer) < 2*a*b:
        answer = 2*a*b
    return int(answer)