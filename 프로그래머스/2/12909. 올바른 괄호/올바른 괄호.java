import java.util.Stack;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c); // 여는 괄호는 무조건 push
            } else {
                if (stack.isEmpty()) {
                    return false; // 닫는 괄호인데 매칭될 여는 괄호 없음
                }
                stack.pop(); // 매칭되는 여는 괄호 pop
            }
        }

        // 끝까지 처리 후 스택이 비어 있어야 정상
        return stack.isEmpty();
    }
}
// class Solution {
//     boolean solution(String s) {
//         int sum = 0;
//         for (char c : s.toCharArray()) {
//             if (c == '(') sum++;
//             else sum--;

//             if (sum < 0) return false;
//         }
//         return sum == 0;
//     }
// }
