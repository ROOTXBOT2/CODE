def solution(arr):
    stk = []
    for num in arr:
        if not stk or stk[-1] != num:  
            stk.append(num)  
        else:
            stk.pop() 
    
    if not stk:
        return [-1] 
    return stk