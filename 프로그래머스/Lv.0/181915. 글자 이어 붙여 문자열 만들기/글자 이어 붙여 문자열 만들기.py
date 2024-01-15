def solution(my_string, index_list):
    # index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙임
    result = "".join(my_string[index] for index in index_list)
    return result