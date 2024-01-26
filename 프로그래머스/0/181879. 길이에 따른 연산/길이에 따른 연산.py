def solution(num_list):
    if len(num_list) >= 11:
        # 리스트의 길이가 11 이상인 경우, 모든 원소의 합을 반환
        return sum(num_list)
    else:
        # 리스트의 길이가 10 이하인 경우, 모든 원소의 곱을 반환
        result = 1
        for num in num_list:
            result *= num
        return result