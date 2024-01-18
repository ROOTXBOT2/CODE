def solution(sizes):
    answer = 0
    w = 0
    h = 0
    for x,y in sizes:
        if x < y:
            x,y= y,x
        if x > w:
            w = x
        if y > h:
            h = y
    answer = w*h
    return answer