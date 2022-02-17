import java.util.Arrays;
import java.util.Scanner;
 
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 테스트 케이스의 수
        int T = sc.nextInt();
        for (int cases = 1; cases <= T; ++cases) {
            // 손님 수
            int N = sc.nextInt();
            int[] customers = new int[N];
            // 몇 초당
            int M = sc.nextInt();
            // 몇 개
            int K = sc.nextInt();
            // 제일 늦게 온 사람 시간
            int max = 0;
            for (int i = 0; i < N; ++i) {
                customers[i] = sc.nextInt();
                if (customers[i] > max) {
                    max = customers[i];
                }
            }
            // 온 순서대로 정렬
            Arrays.sort(customers);
            String ans = "Possible";
            // 붕어빵 개수
            int made = 0;
            // 사람 수
            int idx = 0;
            // 1초씩 증가
            statement: for (int s = 0; s <= max; ++s) {
                // 붕어빵 생성
                if (s != 0 && s % M == 0) {
                    made += K;
                }
                // 손님 왔을 때
                while (idx < N && customers[idx] == s) {
                    // 사람 수 > 붕어빵 개수
                    if (idx + 1 > made) {
                        ans = "Impossible";
                        break statement;
                    }
                    ++idx;
                }
            }
            System.out.println("#" + cases + " " + ans);
        }
    }
}