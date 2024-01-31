def solution(myString):
    # 'x'를 기준으로 문자열을 분리합니다.
    split_str = myString.split('x')
    # 빈 문자열을 제거하고 사전순으로 정렬합니다.
    return sorted(filter(None, split_str))