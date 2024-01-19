from collections import Counter

def solution(my_string):
    count = Counter(my_string)  # 문자열에서 각 문자의 출현 횟수를 세기
    answer = []

    # 대문자 'A'부터 'Z'까지 출현 횟수 추가
    for char in range(ord('A'), ord('Z') + 1):
        answer.append(count.get(chr(char), 0))

    # 소문자 'a'부터 'z'까지 출현 횟수 추가
    for char in range(ord('a'), ord('z') + 1):
        answer.append(count.get(chr(char), 0))
    
    return answer