def solution(arr, k):
    result = []
    seen = set()  # 중복된 숫자를 추적하기 위해 set 사용
    
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
        if len(result) == k:
            break  # k개의 고유한 숫자를 얻으면 종료

    # result의 길이가 k보다 작으면, 남은 부분을 -1로 채우기
    result += [-1 for _ in range(k - len(result))]
        
    return result
