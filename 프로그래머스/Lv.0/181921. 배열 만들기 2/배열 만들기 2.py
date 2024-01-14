def solution(l, r):
    result = []

    # l부터 r까지 순회하며 조건에 맞는 숫자 찾기
    for num in range(l, r + 1):
        if all(digit in ['0', '5'] for digit in str(num)):
            result.append(num)
    
    # 조건에 맞는 숫자가 없으면 -1 반환
    if not result:
        return [-1]

    return result