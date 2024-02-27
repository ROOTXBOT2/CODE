def solution(numbers):
    # 숫자를 문자열로 변환
    numbers_str = [str(number) for number in numbers]
    # 문자열 비교를 위해 정렬
    numbers_str.sort(key=lambda x: x*3, reverse=True)
    # 정렬된 문자열을 합쳐서 결과 생성
    answer = ''.join(numbers_str)
    # 모든 값이 0인 경우를 처리 ("0000"과 같은 경우 "0"으로 반환)
    return answer if answer[0] != '0' else '0'
