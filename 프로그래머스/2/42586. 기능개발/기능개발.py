def solution(progresses, speeds):
    # 각 작업별로 완료까지 남은 일수를 계산합니다.
    days_left = [(100 - p + s - 1) // s for p, s in zip(progresses, speeds)]
    
    # 결과를 저장할 리스트
    result = []
    
    # 첫 번째 작업을 현재 작업으로 설정합니다.
    current_job_days = days_left[0]
    jobs_count = 1  # 현재 배포 그룹에 포함된 작업 수

    # 두 번째 작업부터 확인합니다.
    for days in days_left[1:]:
        if days <= current_job_days:
            # 현재 작업보다 일찍 또는 동시에 끝나는 작업은 같은 배포 그룹에 포함됩니다.
            jobs_count += 1
        else:
            # 다음 작업이 현재 작업보다 늦게 끝나면, 현재 배포 그룹을 종료하고 새 배포 그룹을 시작합니다.
            result.append(jobs_count)
            current_job_days = days
            jobs_count = 1
            
    # 마지막 배포 그룹을 결과에 추가합니다.
    result.append(jobs_count)
    
    return result