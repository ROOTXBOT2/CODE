class Solution {
    public long solution(long n) {
        long left = 1;
        long right = n;

        while (left <= right) {
            long mid = (left + right) / 2;

            if (mid > n / mid) {
                right = mid - 1;
            } else if (mid < n / mid) {
                left = mid + 1;
            } else {
                if (mid * mid == n) {  // 안전하게 한 번만 곱
                    return (mid + 1) * (mid + 1);
                } else {
                    return -1;
                }
            }
        }
        return -1;
    }
}
