import java.util.*;

public class Solution {
    public int[] solution(int[] numbers) {
        int n = numbers.length;
        int[] result = new int[n];
        Stack<Integer> stack = new Stack<>();
        
        Arrays.fill(result, -1);
        
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && numbers[i] > numbers[stack.peek()]) {
                int index = stack.pop();
                result[index] = numbers[i];
            }
            stack.push(i);
        }
        
        return result;
    }
}