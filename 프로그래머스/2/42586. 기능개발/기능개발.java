// import java.util.*;

// class Solution {
//     public List<Integer> solution(int[] progresses, int[] speeds) {
//         List<Integer> answerList = new ArrayList<>();
//         int count = 0;
//         int N = 0;
//         for(int i = 0; i < progresses.length; i++){
//             if((100 - progresses[i] - speeds[i]*N)>0){
//                 if (count > 0) answerList.add(count); // 이전 배포 건 기록
//                 count = 0;
//                 if ((100 - progresses[i])%speeds[i] == 0){
//                     N = (100-progresses[i])/speeds[i];
//                     count++;
//                 } else if((100 - progresses[i])%speeds[i] > 0){
//                     N = (100-progresses[i])/speeds[i] + 1;
//                     count++;
//                 }
//             } else{
//                 count++;
//             }
//         }
//         answerList.add(count); 
//         return answerList;
//     }
// }
import java.util.*;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        Queue<Integer> days = new LinkedList<>();
        List<Integer> result = new ArrayList<>();

        // 1단계: 각 작업의 완료 예상일 계산
        for (int i = 0; i < progresses.length; i++) {
            int remain = 100 - progresses[i];
            int day = (remain + speeds[i] - 1) / speeds[i]; // 올림 처리
            days.offer(day); // 큐에 넣음
        }

        // 2단계: 큐를 돌면서 배포 그룹 계산
        while (!days.isEmpty()) {
            int first = days.poll();
            int count = 1;

            // 다음 기능이 함께 배포될 수 있는지 확인
            while (!days.isEmpty() && days.peek() <= first) {
                days.poll();
                count++;
            }

            result.add(count);
        }

        return result;
    }
}

