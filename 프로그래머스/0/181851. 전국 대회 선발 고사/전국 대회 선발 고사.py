def solution(rank, attendance):
    # 선택한 학생의 인덱스를 저장할 목록을 초기화합니다.
    selected_students = []
    
    # 각 학생의 순위를 인덱스와 페어링하고 출석 기준으로 필터링합니다.
    eligible_students = [(i, r) for i, (r, a) in enumerate(zip(rank, attendance)) if a]
    
    # 적격 학생을 순위별로 정렬합니다.
    sorted_students = sorted(eligible_students, key=lambda x: x[1])
    
    # 순위에 따라 상위 3명의 학생을 선택합니다.
    for i in range(3):
        selected_students.append(sorted_students[i][0])
    
    # 주어진 공식에 따라 결과를 계산합니다.
    result = 10000 * selected_students[0] + 100 * selected_students[1] + selected_students[2]
    return result