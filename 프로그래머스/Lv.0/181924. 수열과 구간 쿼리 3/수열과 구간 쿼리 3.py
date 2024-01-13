def solution(arr, queries):
    answer = []
    for i in queries:
        fir = arr[i[0]]
        sec = arr[i[1]]
        arr[i[0]] = sec
        arr[i[1]] = fir
    return arr