def solution(arr, queries):
    # 각 쿼리를 순회하며 arr를 업데이트
    for query in queries:
        s, e, k = query
        # s부터 e까지의 인덱스에 대해 검사
        for i in range(s, e + 1):
            # i가 k의 배수인 경우 arr[i]에 1을 더함
            if k == 0 or i % k == 0:
                arr[i] += 1
    return arr
