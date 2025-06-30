// import java.util.Arrays;

// class Solution {
//     public int[] solution(int[] array, int[][] commands) {
//         int[] answer = new int[commands.length];
//         for(int i = 0; i < commands.length; i++){
//             int start = commands[i][0] - 1;
//             int end = commands[i][1];
//             int k = commands[i][2] - 1;
            
//             // 배열 자르기
//             int[] temp = Arrays.copyOfRange(array, start, end);

//             // 정렬
//             Arrays.sort(temp);

//             // k번째 수 저장
//             answer[i] = temp[k]; 
//         }
//         return answer;
//     }
// }


class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for (int i = 0; i < commands.length; i++) {
            int start = commands[i][0] - 1;
            int end = commands[i][1] - 1;
            int k = commands[i][2] - 1;

            // 1. 자르기 (부분 배열 생성)
            int length = end - start + 1;
            int[] temp = new int[length];
            int idx = 0;
            for (int j = start; j <= end; j++) {
                temp[idx++] = array[j];
            }

            // 2. 정렬 (버블 정렬 예시)
            for (int a = 0; a < temp.length - 1; a++) {
                for (int b = 0; b < temp.length - a - 1; b++) {
                    if (temp[b] > temp[b + 1]) {
                        // swap
                        int t = temp[b];
                        temp[b] = temp[b + 1];
                        temp[b + 1] = t;
                    }
                }
            }

            // 3. k번째 수 저장
            answer[i] = temp[k];
        }

        return answer;
    }
}
