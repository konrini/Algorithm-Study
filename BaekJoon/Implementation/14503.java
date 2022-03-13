import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	// 북 동 남 서
	static int[][] dir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };

	// map size
	static int N, M;

	// 로봇 청소기 좌표와 방향
	static int r, c, D;

	// 지도
	static int[][] map;

	// 로봇 청소기가 청소하는 칸의 개수
	static int cnt = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
		// map size
		N = Integer.parseInt(st1.nextToken());
		M = Integer.parseInt(st1.nextToken());
		// 로봇 청소기 좌표와 방향
		StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
		r = Integer.parseInt(st2.nextToken());
		c = Integer.parseInt(st2.nextToken());
		D = Integer.parseInt(st2.nextToken());
		// 지도
		map = new int[N][M];
		for (int i = 0; i < N; i++) {
			StringTokenizer st3 = new StringTokenizer(br.readLine(), " ");
			for (int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(st3.nextToken());
			}
		}

		// 로봇 청소기 청소 시작
		dfs(r, c, D);

		// 출력
		bw.write(cnt + "");
		bw.close();
	}

	public static void dfs(int r, int c, int D) {

		// 현재 위치를 청소한다.
		if (map[r][c] == 0) {
			++cnt;
		}
		map[r][c] = -1;
		// 몇 번 회전하는지 체크
		int i;
		for (i = 1; i <= 4; i++) {
			// 왼쪽 회전하면 보이는 방향
			int nd = (D - i + 4) % 4;
			// 왼쪽 회전하면 보이는 좌표
			int nr = r + dir[nd][0];
			int nc = c + dir[nd][1];

			if (map[nr][nc] == 0) {
				dfs(nr, nc, nd);
				break;
			}
		}
		// 네 방향 다 탐색했을 때
		if (i == 5) {
			// 후진
			int bd = (D + 2) % 4;
			int br = r + dir[bd][0];
			int bc = c + dir[bd][1];
			if (map[br][bc] == 1) {
				return;
			} else {
				dfs(br, bc, D);
			}
		}
	}
}