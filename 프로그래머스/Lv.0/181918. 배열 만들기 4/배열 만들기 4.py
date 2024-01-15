def solution(arr):
    stk = []
    i = 0
    while True:
        if i < len(arr):
            if len(stk) == 0:
                stk.append(arr[i])
                i+=1
            elif stk[-1] < arr[i]:
                stk.append(arr[i])
                i+=1
            elif stk[-1] >= arr[i]:
                stk.pop()
            else:
                return -1
        else:
            return stk