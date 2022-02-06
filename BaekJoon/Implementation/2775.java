import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; ++i) {
			List<List<Integer>> arr = new ArrayList<>();
			int k = Integer.parseInt(br.readLine());
			int n = Integer.parseInt(br.readLine());
			int level = 0;
			while (level <= k) {
				int num = 0;
				List<Integer> arr1 = new ArrayList<>();
				while (num < n) {
					if (level == 0) {
						arr1.add(num + 1);
					} else {
						if (num == 0) {
							arr1.add(arr.get(level - 1).get(num));
						} else {
							arr1.add(arr.get(level - 1).get(num) + arr1.get(num - 1));
						}
					}
					++num;
				}
				arr.add(arr1);
				++level;
			}
			bw.write(arr.get(k).get(n - 1) + "\n");
		}
		bw.close();
	}
}