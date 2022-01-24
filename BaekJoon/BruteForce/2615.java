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

		int[][] table = new int[19][19];
		for (int i = 0; i < 19; ++i) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 19; ++j) {
				table[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int[] dx = { 1, 0, 1, -1 };
		int[] dy = { 1, 1, 0, 1 };

		boolean check = false;
		for (int x = 0; x < 19; ++x) {
			for (int y = 0; y < 19; ++y) {
				if (table[x][y] == 1) {
					for (int dir1 = 0; dir1 < 4; ++dir1) {
						if (x - dx[dir1] >= 0 && y - dy[dir1] >= 0 && x - dx[dir1] < 19 && y - dy[dir1] < 19) {
							if (table[x - dx[dir1]][y - dy[dir1]] == 1)
								continue;
						}
						int dist = 0;
						while (true) {
							dist += 1;
							int nx = x + dist * dx[dir1];
							int ny = y + dist * dy[dir1];
							if (nx < 0 || ny < 0 || nx >= 19 || ny >= 19) {
								if (dist == 5) {
									bw.write("1\n");
									bw.write(String.valueOf(x + 1) + " " + String.valueOf(y + 1));
									check = true;
								}
								break;
							}
							if (dist == 5 && table[nx][ny] == 1) {
								break;
							}
							if (dist == 5 && table[nx][ny] != 1) {
								bw.write("1\n");
								bw.write(String.valueOf(x + 1) + " " + String.valueOf(y + 1));
								check = true;
								break;
							}
							if (table[nx][ny] != 1)
								break;
						}
						if (check == true)
							break;
					}
				} else if (table[x][y] == 2) {
					for (int dir2 = 0; dir2 < 4; ++dir2) {
						if (x - dx[dir2] >= 0 && y - dy[dir2] >= 0 && x - dx[dir2] < 19 && y - dy[dir2] < 19) {
							if (table[x - dx[dir2]][y - dy[dir2]] == 2)
								continue;
						}
						int dist = 0;
						while (true) {
							dist += 1;
							int nx = x + dist * dx[dir2];
							int ny = y + dist * dy[dir2];
							if (nx < 0 || ny < 0 || nx >= 19 || ny >= 19) {
								if (dist == 5) {
									bw.write("2\n");
									bw.write(String.valueOf(x + 1) + " " + String.valueOf(y + 1));
									check = true;
								}
								break;
							}
							if (dist == 5 && table[nx][ny] == 2) {
								break;
							}
							if (dist == 5 && table[nx][ny] != 2) {
								bw.write("2\n");
								bw.write(String.valueOf(x + 1) + " " + String.valueOf(y + 1));
								check = true;
								break;
							}
							if (table[nx][ny] != 2)
								break;
						}
						if (check == true)
							break;
					}
				}
				if (check == true)
					break;
			}
			if (check == true)
				break;
		}
		if (check == true)
			bw.close();
		else {
			bw.write("0");
			bw.close();
		}
	}
}
