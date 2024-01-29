def solution(myString, pat):
    count = 0
    pat_length = len(pat)
    
    for i in range(len(myString) - pat_length + 1):
        if myString[i:i+pat_length] == pat:
            count += 1
    
    return count
