import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    // 소수 구하기
    public static List<Integer> sieve(int N) {
        boolean[] isPrime = new boolean[N + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;

        for (int i = 2; i * i <= N; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= N; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= N; i++) {
            if (isPrime[i]) primes.add(i);
        }
        return primes;
    }

    // 세 소수의 합으로 표현
    private static void printThreePrimeSum(int n, List<Integer> primes) {
        Set<Integer> primeSet = new HashSet<>(primes);
        boolean found = false;

        for (int i = 0; i < primes.size() && !found; i++) {
            int a = primes.get(i);
            for (int j = i; j < primes.size() && !found; j++) {
                int b = primes.get(j);
                int c = n - a - b;
                if (c < b) continue; // b ≤ c 유지
                if (primeSet.contains(c)) {
                    System.out.println(a + " " + b + " " + c);
                    found = true;
                    break;
                }
            }
        }

        if (!found) {
            System.out.println("0"); // 가능한 조합 없을 때 (문제 조건상 나오진 않음)
        }
    }

    public static void main(String[] args) throws IOException {
        // 입력 처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int t = 0; t < T; t++) {
            int n = Integer.parseInt(br.readLine());
            List<Integer> primes = sieve(n); // 매번 sieve 호출 (n이 커야 하므로)
            printThreePrimeSum(n, primes);
        }
    }
}
