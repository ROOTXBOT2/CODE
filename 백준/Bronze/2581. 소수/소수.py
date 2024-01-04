start_num = int(input())
last_num = int(input())

# 에라토스테네스의 체 초기화
sieve = [True] * (last_num + 1)
sieve[0:2] = [False, False]  # 0과 1은 소수가 아님

# 에라토스테네스의 체 알고리즘
for i in range(2, int(last_num**0.5) + 1):
    if sieve[i]:
        for j in range(i*2, last_num + 1, i):
            sieve[j] = False

# 소수 리스트 생성
sosu_list = [i for i in range(start_num, last_num + 1) if sieve[i]]

# 결과 출력
if sosu_list:
    print(sum(sosu_list))
    print(min(sosu_list))
else:
    print(-1)