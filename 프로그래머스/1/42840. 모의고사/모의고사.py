def solution(answers):
    # Define the patterns for each student
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # Initialize scores for each student
    scores = [0, 0, 0]
    
    # Calculate scores
    for idx, answer in enumerate(answers):
        for student, pattern in enumerate(patterns):
            if answer == pattern[idx % len(pattern)]:
                scores[student] += 1
    
    # Find the highest score
    highest = max(scores)
    
    # Find students with the highest score
    result = [i+1 for i, score in enumerate(scores) if score == highest]
    
    return result
