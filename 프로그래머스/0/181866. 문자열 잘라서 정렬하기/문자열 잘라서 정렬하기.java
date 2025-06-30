import java.util.Arrays;

class Solution {
    public String[] solution(String myString) {
        String[] answer = {};
        return Arrays.stream(myString.split("x"))
                     .filter(s -> !s.isEmpty())   // 빈 문자열 제거
                     .sorted()                   // 사전순 정렬
                     .toArray(String[]::new);    // 배열로 변환
    }
}