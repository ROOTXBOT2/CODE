import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # scoville 배열을 최소 힙으로 변환
    mix_count = 0

    while scoville:
        # 가장 낮은 스코빌 지수를 가진 음식 추출
        first_min = heapq.heappop(scoville)

        # 첫 번째로 맵지 않은 음식의 스코빌 지수가 이미 K 이상이면 더 이상 섞을 필요가 없음
        if first_min >= K:
            return mix_count

        # scoville 배열이 비어있으면 모든 음식을 K 이상으로 만들 수 없음
        if not scoville:
            return -1

        # 두 번째로 맵지 않은 음식 추출
        second_min = heapq.heappop(scoville)

        # 새로운 음식을 만들고 스코빌 지수 계산
        new_scoville = first_min + second_min * 2

        # 새로운 음식을 힙에 추가
        heapq.heappush(scoville, new_scoville)
        mix_count += 1

    return -1