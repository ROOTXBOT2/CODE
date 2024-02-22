def solution(a, b):
    # 두 주사위 숫자가 모두 홀수일 때
    if a % 2 == 1 and b % 2 == 1:
        return a**2 + b**2
    # 두 주사위 중 하나만 홀수일 때
    elif a % 2 == 1 or b % 2 == 1:
        return 2 * (a + b)
    # 두 주사위 숫자가 모두 홀수가 아닐 때
    else:
        return abs(a - b)