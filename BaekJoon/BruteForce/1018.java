import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		// 체스판 만들기
		String[][] chess = new String[N][M];
		for (int n = 0; n < N; ++n) {
			String temp = br.readLine();
			for (int m = 0; m < M; ++m) {
				chess[n][m] = temp.charAt(m) + "";
			}
		}
		// 다시 칠해야 하는 정사각형 갯수의 최솟값
		int min = 32;
		// 정사각형 보기
		for (int y = 0; y <= N - 8; ++y) {
			for (int x = 0; x <= M - 8; ++x) {
				// 시작 칸을 바꾸는 경우와 바꾸지 않은 경우 둘 다 본다.
				for (int cases = 0; cases < 2; ++cases) {
					// 처음 case에는 색깔 바꾸고, 다시 원상 복구하기.
					if (chess[y][x].equals("W")) {
						chess[y][x] = "B";
					} else {
						chess[y][x] = "W";
					}
					// 색칠할 개수
					int cnt = 0;
					// 처음 case에는 색깔을 바꿨기 때문이다.
					if (cases == 0) {
						cnt += 1;
					}
					// 시작 칸의 좌표의 합이 홀수/짝수일 때
					// 탐색할 칸의 좌표의 합이 홀수/짝수이면 시작 칸과 색깔이 같다.
					int target = (x + y) % 2;
					for (int b = y; b < y + 8; ++b) {
						for (int a = x; a < x + 8; ++a) {
							// 색깔이 원래 같아야 하는 경우
							if ((a + b) % 2 == target) {
								if (!(chess[b][a].equals(chess[y][x]))) {
									cnt += 1;
								}
							}
							// 색깔이 원래 달라야 하는 경우
							else {
								if (chess[b][a].equals(chess[y][x])) {
									cnt += 1;
								}
							}
						}
					}
					if (min > cnt) {
						min = cnt;
					}
				}
			}
		}
		bw.write(min + "");
		bw.close();
	}
}
