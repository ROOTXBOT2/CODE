class Solution {
    // GCD(유클리드 호제법)
    public static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
    
    // LCM 공식
    public static int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }
    
    public int[] solution(int n, int m) {
        int gcdValue = gcd(n, m);  
        int lcmValue = lcm(n, m);
        int[] answer = new int[] {gcdValue, lcmValue}; // ← 이렇게!
        return answer;
    }
}