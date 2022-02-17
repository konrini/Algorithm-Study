import java.util.Scanner;
 
public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 테스트 케이스의 수
        int T = sc.nextInt();
        for (int cases = 1; cases <= T; ++cases) {
            // 첫 번째 테스트 케이스
            int N = sc.nextInt();
            // 두 번째 테스트 케이스
            int M = sc.nextInt();
            // 합 개수를 담을 배열
            int[] cnt = new int[N + M + 1];
            for (int i = 1; i <= N; ++i) {
                for (int j = 1; j <= M; ++j) {
                    ++cnt[i + j];
                }
            }
            // 최댓값 확인
            int max = 0;
            for (int num : cnt) {
                if (num > max) {
                    max = num;
                }
            }
            // 출력
            System.out.print("#" + cases + " ");
            for (int idx = 0; idx < N + M + 1; ++idx) {
                if (cnt[idx] == max) {
                    System.out.print(idx + " ");
                }
            }
            System.out.println();
        }
    }
}