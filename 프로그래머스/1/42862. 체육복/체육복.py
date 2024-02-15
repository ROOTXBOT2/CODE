def solution(n, lost, reserve):
    # Convert lists to sets for efficient operations
    set_lost = set(lost)
    set_reserve = set(reserve)
    
    # Handle students who lost and have a reserve
    set_both = set_lost & set_reserve
    set_lost -= set_both
    set_reserve -= set_both
    
    # Try to lend uniforms
    for r in sorted(set_reserve):
        if r - 1 in set_lost:
            set_lost.remove(r - 1)
        elif r + 1 in set_lost:
            set_lost.remove(r + 1)
    
    # Calculate the number of students who can attend the class
    return n - len(set_lost)