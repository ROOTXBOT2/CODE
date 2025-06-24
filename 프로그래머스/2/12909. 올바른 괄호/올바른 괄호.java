class Solution {
    boolean solution(String s) {
        boolean answer = true;
        char[] chars = s.toCharArray();
        int sum = 0;
        for (int i = 0; i < chars.length; i++){
            if (i == 0 && chars[i] == ')'){
                sum--;
                answer = false;
                break;
            } else if(sum < 0){
                answer = false;
                break;
            }
            
            if (chars[i] == '('){
                sum++;
            }
            else if (chars[i] == ')'){
                sum--;
            }
        }
        if (sum == 0){
            answer = true;
        } else{
            answer = false;
        }
        return answer;
    }
}