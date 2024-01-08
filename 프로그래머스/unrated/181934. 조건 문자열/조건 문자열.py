def solution(ineq, eq, n, m):
    answer = 0
    if eq =="!":
        eq =""
    if int(eval(f"{n} {ineq}{eq} {m}")):
        answer = 1
    return answer