def solution(num_list):
    num_list.sort(reverse=True)
    answer = num_list[:-5]
    return sorted(answer)