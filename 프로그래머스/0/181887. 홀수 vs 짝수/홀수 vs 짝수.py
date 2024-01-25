def solution(num_list):
    fir,sec = 0,0
    
    for i in range(len(num_list)):
        if (i+1) % 2 == 1:
            fir += num_list[i]
        else:
            sec += num_list[i]
    if fir > sec: 
        return fir
    else:
        return sec
            
     