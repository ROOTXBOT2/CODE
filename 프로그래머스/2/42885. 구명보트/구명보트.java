import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        Arrays.sort(people);
        int i = 0;
        int j = people.length - 1;
        int Sum = people[i];
        while (i <= j) {
            if (people[i] + people[j] <= limit) {
                i++;  // 가벼운 사람 태움
            }
            j--;      // 무거운 사람은 무조건 태움
            answer++; // 보트 1대 사용
        }
        return answer;
    }
}

