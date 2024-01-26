def solution(num_list):
    def reduce_to_one(n):
        count = 0
        while n > 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = (n - 1) / 2
            count += 1
        return count

    total_operations = sum(reduce_to_one(num) for num in num_list)
    return total_operations