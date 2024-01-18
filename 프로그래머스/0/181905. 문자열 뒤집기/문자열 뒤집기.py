def solution(my_string, s, e):
    reversed_part = my_string[s:e+1][::-1]
    return my_string[:s] + reversed_part + my_string[e+1:]
