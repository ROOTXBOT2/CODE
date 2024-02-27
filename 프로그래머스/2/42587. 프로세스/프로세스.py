from collections import deque

def solution(priorities, location):
    # (우선순위, 위치) 튜플로 대기 큐를 초기화
    queue = deque([(priority, i) for i, priority in enumerate(priorities)])
    answer = 0  # 실행 순서

    while queue:
        current = queue.popleft()  # 현재 프로세스를 큐에서 꺼냄
        # 큐에 남아 있는 프로세스 중 현재 프로세스보다 우선순위가 높은 프로세스가 있는지 확인
        if any(current[0] < other[0] for other in queue):
            queue.append(current)  # 더 높은 우선순위의 프로세스가 있다면 현재 프로세스를 큐의 끝에 다시 넣음
        else:
            answer += 1  # 현재 프로세스를 실행
            # 현재 실행한 프로세스가 알고자 하는 프로세스의 위치와 일치하면 반복 종료
            if current[1] == location:
                break

    return answer