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
        // 최댓값
        int max_num = -1;
        // N의 첫째 자리보다 작으면서 최댓값
        int max_num2 = -1;
        // 0 포함 최솟값
        int min_num = 10;
        // 0 미포함 최솟값
        int min_num2 = 10;
        // N의 첫째 자리보다 크면서 최솟값
        int min_num3 = 10;
        for (int i = 0; i < use_btn.length; i++) {
            if (use_btn[i] == 1) {
                if (i > max_num) {
                    max_num = i;
                }
                if (i < (N + "").charAt(0) - '0' && i > max_num2) {
                    max_num2 = i;
                }
                if (i < min_num) {
                    min_num = i;
                }
                if (i > 0 && i < min_num2) {
                    min_num2 = i;
                }
                if (i > (N + "").charAt(0) - '0' && i < min_num3) {
                    min_num3 = i;
                }
            }
        }
        // 100번 채널에서 플러스 버튼 혹은 마이너스 버튼만으로 채널 이동할 때
        int answer1 = Math.abs(N - 100);
        // 버튼이 고장나서 최대한 가까운 채널로 가서 플러스 버튼 혹은 마이너스 버튼으로 채널 이동할 때
        String num = N + "";
        // 작은 숫자여서 플러스 버튼 누를 때
        // 처음 다른 값은 작은 숫자여야하고, 그 이후로는 큰 값이어야 한다.
        int cnt = 0;
        String clicked1 = "";
        statement1: while (clicked1.length() < num.length()) {
            if (cnt == 0) {
                // 고장나지 않은 버튼일 때
                if (use_btn[num.charAt(clicked1.length()) - '0'] == 1) {
                    clicked1 += num.charAt(clicked1.length());
                }
                // 고장난 버튼일 때
                else {
                    for (int i = num.charAt(clicked1.length()) - '0' - 1; i >= 0; i--) {
                        if (use_btn[i] == 1) {
                            ++cnt;
                            clicked1 += i;
                            break;
                        }
                    }
                    // 작은 버튼이 모두 고장났을 때
                    // 자리수가 하나 작게 만들어 -> 숫자 제일 커져야 돼
                    if (cnt == 0) {
                        clicked1 = "";
                        if (max_num2 == -1) {
                            for (int i = 0; i < num.length() - 1; i++) {
                                clicked1 += String.valueOf(max_num);
                            }
                        } else {
                            clicked1 += String.valueOf(max_num2);
                            for (int i = 0; i < num.length() - 1; i++) {
                                clicked1 += String.valueOf(max_num);
                            }
                        }
                        break statement1;
                    }
                }
            } else if (cnt == 1) {
                clicked1 += String.valueOf(max_num);
            }
        }
        if (clicked1 == "") {
            clicked1 = "1000000";
        }
        int answer2 = Math.abs(N - Integer.parseInt(clicked1)) + (Integer.parseInt(clicked1) + "").length();
        // 큰 숫자여서 마이너스 버튼 누를 때
        // 처음 다른 값은 큰 숫자여야하고, 그 이후로는 작은 값이어야 한다.
        cnt = 0;
        String clicked2 = "";
        statement2: while (clicked2.length() < num.length()) {
            if (cnt == 0) {
                // 고장나지 않은 버튼일 때
                if (use_btn[num.charAt(clicked2.length()) - '0'] == 1) {
                    clicked2 += num.charAt(clicked2.length());
                }
                // 고장난 버튼일 때
                else {
                    for (int i = num.charAt(clicked2.length()) - '0' + 1; i <= 9; i++) {
                        if (use_btn[i] == 1) {
                            ++cnt;
                            clicked2 += i;
                            break;
                        }
                    }
                    // 큰 버튼이 모두 고장났을 때
                    // 자리수가 하나 크게 만들어 -> 숫자 제일 작아져야 돼
                    if (cnt == 0) {
                        clicked2 = "";
                        if (min_num3 == 10) {
                            if (min_num2 == 10) {
                                clicked2 = "1000000";
                            } else {
                                clicked2 += String.valueOf(min_num2);
                                for (int i = 0; i < num.length(); i++) {
                                    clicked2 += String.valueOf(min_num);
                                }
                            }
                        } else {
                            clicked2 += String.valueOf(min_num3);
                            for (int i = 0; i < num.length() - 1; i++) {
                                clicked2 += String.valueOf(min_num);
                            }
                        }
                        break statement2;
                    }
                }
            } else if (cnt == 1) {
                clicked2 += min_num;
            }
        }
        int answer3 = Math.abs(Integer.parseInt(clicked2) - N) + (Integer.parseInt(clicked2) + "").length();
        // 최소 버튼 클릭
        int min = Math.min(answer1, Math.min(answer2, answer3));
        System.out.println(min);
    }
}