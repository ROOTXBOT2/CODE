def solution(myString):
    return ''.join(['A' if char == 'a' else char.lower() if char != 'A' else char for char in myString])
