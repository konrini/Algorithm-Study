import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int[][] dir = { { 0, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
		// 통로의 세로 길이
		int N = Integer.parseInt(st1.nextToken());
		// 통로의 가로 길이
		int M = Integer.parseInt(st1.nextToken());
		// 음식물 쓰레기의 개수
		int K = Integer.parseInt(st1.nextToken());
		// 지도
		int[][] trash = new int[N][M];
		for (int i = 0; i < K; i++) {
			StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
			trash[Integer.parseInt(st2.nextToken()) - 1][Integer.parseInt(st2.nextToken()) - 1] = 1;
		}
		int max = 0;
		List<Integer[]> queue = new ArrayList<>();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (trash[i][j] == 1) {
					int cnt = 1;
					Integer[] start = { i, j };
					queue.add(start);
					trash[i][j] = 0;
					while (queue.size() > 0) {
						int r = queue.get(0)[0];
						int c = queue.get(0)[1];
						queue.remove(0);
						for (int l = 0; l < 4; l++) {
							int rr = r + dir[l][0];
							int cc = c + dir[l][1];
							if (rr < 0 || rr >= N || cc < 0 || cc >= M) {
								continue;
							}
							if (trash[rr][cc] == 1) {
								Integer[] next = { rr, cc };
								queue.add(next);
								trash[rr][cc] = 0;
								++cnt;
							}
						}
					}
					if (cnt > max) {
						max = cnt;
					}
				}

			}
		}
		bw.write(max + "");
		bw.close();
	}
}