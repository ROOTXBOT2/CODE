def solution(numbers, target):
    # 1. DFS 함수 정의
    def dfs(index, current_sum):
        # 1.1. 재귀 함수의 종료 조건: 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            # 1.1.1. 현재 합계가 타겟 넘버와 같으면 1을 반환
            if current_sum == target:
                return 1
            # 1.1.2. 그렇지 않으면 0을 반환
            else:
                return 0
        # 1.2. 현재 숫자를 더하는 경우와 빼는 경우를 모두 탐색
        else:
            # 1.2.1. 현재 숫자를 더하는 경우
            count = dfs(index + 1, current_sum + numbers[index])
            # 1.2.2. 현재 숫자를 빼는 경우
            count += dfs(index + 1, current_sum - numbers[index])
            # 1.2.3. 두 경우의 결과를 합산하여 반환
            return count

    # 2. DFS 탐색 시작
    answer = dfs(0, 0)
    # 3. 타겟 넘버를 만드는 방법의 수 반환
    return answer