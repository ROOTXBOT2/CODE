def solution(names):
    answer = [names[i] for i in range(len(names)) if i % 5 == 0 ]
    return answer
