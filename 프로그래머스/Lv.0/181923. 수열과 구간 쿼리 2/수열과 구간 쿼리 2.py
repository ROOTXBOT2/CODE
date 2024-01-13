def solution(arr, queries):
    result = []
    
    for s,e,k in queries:
        filtered = [i for i in arr[s:e+1] if i > k]
        answer = min(filtered) if filtered else -1
        result.append(answer)

    return result

