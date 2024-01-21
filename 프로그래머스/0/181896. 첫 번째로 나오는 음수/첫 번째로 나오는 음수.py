def solution(num_list):
    answer = 0
    answer = [i for i in range(len(num_list)) if num_list[i] < 0]
    if answer:
        return answer[0]
    else:
        return -1
