def solution(phone_book):
    phone_book.sort()  # 전화번호부를 정렬
    for i in range(len(phone_book) - 1):
        # 현재 번호가 다음 번호의 접두사인 경우
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True