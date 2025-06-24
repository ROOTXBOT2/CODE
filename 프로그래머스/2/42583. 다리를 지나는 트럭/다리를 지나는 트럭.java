import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        //bridge_length : 다리를 한대가 건너는데 걸리는 시간임과 동시에 비어있는 공간으로 차가 올라갈 수 있는 공간이기도함.
        //weight는 제한 무게. 이걸로 큐의 조건문을 만들어야함.
        Queue<Integer> bridge = new LinkedList<>();
        int time = 0;                 // 경과 시간
        int totalWeight = 0;         // 현재 다리 위 총 무게
        int idx = 0;                 // 현재 올라가야 할 트럭 인덱스
        
        for (int i = 0; i < bridge_length; i++) {
            bridge.offer(0);
        }
        while (!bridge.isEmpty()) {
            time++; // 시간 흐름
            
            // 다리에서 한 칸 이동 → 맨 앞 트럭 제거
            totalWeight -= bridge.poll();
            
            // 아직 올라갈 트럭이 남아 있을 때
            if (idx < truck_weights.length) {
                int nextTruck = truck_weights[idx];

                // 다음 트럭을 올릴 수 있는 경우
                if (totalWeight + nextTruck <= weight) {
                    bridge.offer(nextTruck); // 트럭 투입
                    totalWeight += nextTruck;
                    idx++;
                } else {
                    // 무게 초과 → 0만 넣어서 자리만 채움
                    bridge.offer(0);
                }
            }
        }
        return time;
    }
}