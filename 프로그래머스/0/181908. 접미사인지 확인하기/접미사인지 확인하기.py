def solution(my_string, is_suffix):
    suffixs = [my_string[-i:] for i in range(len(my_string))]
    answer = 1 if is_suffix in suffixs else 0
    return answer