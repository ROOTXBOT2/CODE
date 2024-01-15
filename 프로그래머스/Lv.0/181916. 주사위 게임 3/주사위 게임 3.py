def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice_count = {num: dice.count(num) for num in set(dice)}

    # 네 주사위의 숫자가 모두 같은 경우
    if 4 in dice_count.values():
        return 1111 * a

    # 세 주사위의 숫자가 같은 경우
    if 3 in dice_count.values():
        for num, count in dice_count.items():
            if count == 3:
                p = num
            else:
                q = num
        return (10 * p + q) ** 2

    # 두 개씩 같은 값이 나오는 경우
    if len(dice_count) == 2 and all(count == 2 for count in dice_count.values()):
        p, q = dice_count.keys()
        return (p + q) * abs(p - q)

    # 어느 두 주사위에서 같은 숫자가 나오는 경우
    if 2 in dice_count.values():
        for num, count in dice_count.items():
            if count == 2:
                p = num
            else:
                if 'q' in locals():
                    r = num
                else:
                    q = num
        return q * r

    # 네 주사위 숫자가 모두 다른 경우
    return min(dice)