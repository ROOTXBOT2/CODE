def solution(arr):
    def process_element(e):
        if e >= 50 and e % 2 == 0:
            return e // 2
        elif e < 50 and e % 2 == 1:
            return e * 2 + 1
        else:
            return e

    def process_array(a):
        return [process_element(e) for e in a]

    x = 0
    while True:
        next_arr = process_array(arr)
        if next_arr == arr:
            break
        arr = next_arr
        x += 1

    return x