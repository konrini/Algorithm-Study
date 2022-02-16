import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());
		int[][] coor = new int[N][2];
		for (int i = 0; i < N; ++i) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			coor[i][0] = Integer.parseInt(st.nextToken());
			coor[i][1] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(coor, new Comparator<int[]>() {
			@Override
			public int compare(int[] coor1, int[] coor2) {
				if (coor1[1] == coor2[1]) {
					return coor1[0] - coor2[0];
				}
				return coor1[1] - coor2[1];
			}
		});
		for (int i = 0; i < N; ++i) {
			bw.write(coor[i][0] + " " + coor[i][1] + "\n");
		}
		bw.close();
	}
}