def solution(myStr):
    parts = []
    temp_str = ''
    for char in myStr:
        if char in ['a', 'b', 'c']:
            if temp_str:
                parts.append(temp_str)
            temp_str = ''
        else:
            temp_str += char
    if temp_str:
        parts.append(temp_str)
    
    # Check if the resulting array is empty
    if not parts:
        return ["EMPTY"]
    
    return parts