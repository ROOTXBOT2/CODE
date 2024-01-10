def solution(code):
    answer = ''
    mode = 0
    for idx in range(len(code)):
        if code[idx] =="1":
            if mode == 1:
                mode = 0
            else:
                mode = 1
        else:
            if mode == 0:
                if idx % 2 == 0:
                    answer = answer + code[idx]
            else:           
                if idx % 2 == 1:
                    answer = answer + code[idx]
    if answer == "":
        return "EMPTY"
    return answer