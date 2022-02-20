import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());
		int[][] board = new int[100][100];
		for (int i = 0; i < N; ++i) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int v = Integer.parseInt(st.nextToken());
			int h = Integer.parseInt(st.nextToken());
			int max_v = v + 10 > 100 ? 100 : v + 10;
			int max_h = h + 10 > 100 ? 100 : h + 10;
			for (int a = v; a < max_v; ++a) {
				for (int b = h; b < max_h; ++b) {
					++board[a][b];
				}
			}
		}
		int ans = 0;
		for (int r = 0; r < 100; ++r) {
			for (int c = 0; c < 100; ++c) {
				if (board[r][c] != 0) {
					if (r == 0 || board[r - 1][c] == 0) {
						++ans;
					}
					if (c == 0 || board[r][c - 1] == 0) {
						++ans;
					}
					if (r == 99 || board[r + 1][c] == 0) {
						++ans;
					}
					if (c == 99 || board[r][c + 1] == 0) {
						++ans;
					}
				}
			}
		}
		bw.write(ans + "");
		bw.close();
	}
}