import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 이동하려고 하는 채널
        int N = Integer.parseInt(br.readLine());
        // 고장난 버튼의 개수
        int M = Integer.parseInt(br.readLine());
        // 만약 고장난 버튼이 없을 때
        if (M == 0) {
            System.out.println(Math.min(Math.abs(100 - N), (N + "").length()));
            return;
        }
        // 고장나지 않은 버튼 (누를 수 있는 버튼)
        int[] use_btn = { 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 };
        StringTokenizer st = new StringTokenizer(br.readLine() + " ");
        for (int i = 0; i < M; i++) {
            use_btn[Integer.parseInt(st.nextToken())] = 0;
        }
        // 만약 모든 버튼이 고장났을 때
        if (M == 10) {
            System.out.println(Math.abs(100 - N));
            return;
        }
        // 100번 채널에서 플러스 버튼 혹은 마이너스 버튼만으로 채널 이동할 때
        int answer1 = Math.abs(N - 100);
        // 최대한 가까운 채널로 가서 플러스 버튼 혹은 마이너스 버튼으로 채널 이동할 때
        String num = N + "";
        // 버튼이 고장나지 않았을 때
        boolean check = true;
        for (int i = 0; i < num.length(); i++) {
            if (use_btn[num.charAt(i) - '0'] == 0) {
                check = false;
                break;
            }
        }
        if (check) {
            System.out.println(Math.min(answer1, num.length()));
            return;
        }
        // 버튼 고장났을 때
        // 작은 숫자여서 플러스 버튼 누를 때
        int answer2 = 1000000;
        boolean check1;
        for (int i = N - 1; i >= 0; i--) {
            String num1 = i + "";
            check1 = true;
            for (int j = 0; j < num1.length(); j++) {
                if (use_btn[num1.charAt(j) - '0'] == 0) {
                    check1 = false;
                    break;
                }
            }
            if (check1) {
                answer2 = num1.length() + (N - i);
                break;
            }
        }
        // 큰 숫자여서 마이너스 버튼 누를 때
        int answer3 = 1000000;
        boolean check2;
        for (int i = N + 1; i <= 1000000; i++) {
            String num2 = i + "";
            check2 = true;
            for (int j = 0; j < num2.length(); j++) {
                if (use_btn[num2.charAt(j) - '0'] == 0) {
                    check2 = false;
                    break;
                }
            }
            if (check2) {
                answer3 = num2.length() + (i - N);
                break;
            }
        }
        // 최소 버튼 클릭
        int min = Math.min(answer1, Math.min(answer2, answer3));
        System.out.println(min);
    }
}