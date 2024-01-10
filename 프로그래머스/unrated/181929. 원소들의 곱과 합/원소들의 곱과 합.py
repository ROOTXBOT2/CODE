def solution(num_list):
    a = 1
    b = 0
    for i in num_list: 
        a = i*a
        b = b + i
    
    if a < b**2:
        return 1
    return 0