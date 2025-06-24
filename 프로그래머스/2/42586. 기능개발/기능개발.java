import java.util.*;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answerList = new ArrayList<>();
        int count = 0;
        int N = 0;
        for(int i = 0; i < progresses.length; i++){
            if((100 - progresses[i] - speeds[i]*N)>0){
                if (count > 0) answerList.add(count); // 이전 배포 건 기록
                count = 0;
                if ((100 - progresses[i])%speeds[i] == 0){
                    N = (100-progresses[i])/speeds[i];
                    count++;
                } else if((100 - progresses[i])%speeds[i] > 0){
                    N = (100-progresses[i])/speeds[i] + 1;
                    count++;
                }
            } else{
                count++;
            }
        }
        answerList.add(count); 
        return answerList;
    }
}