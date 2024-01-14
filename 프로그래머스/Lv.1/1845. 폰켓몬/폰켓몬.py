from collections import Counter
def solution(nums):
    answer = 0
    
    if len(nums)/2 >= len(Counter(nums)):
        answer = len(Counter(nums))
    elif len(nums)/2 < len(Counter(nums)):
        answer = len(nums)/2
    return answer