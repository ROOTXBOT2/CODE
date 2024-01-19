def solution(n, k):
    answer = []
    answer = [ k*i for i in range(1,int(n/k)+1) ]
    return answer