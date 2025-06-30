import java.util.Arrays;

public class Solution {
    public static String solution(String my_string) {
        // 1. 모두 소문자로
        my_string = my_string.toLowerCase();

        // 2. 문자 배열로 변환
        char[] chars = my_string.toCharArray();

        // 3. 정렬
        Arrays.sort(chars);

        // 4. 정렬된 문자 배열을 문자열로 변환
        return new String(chars);
    }
}
