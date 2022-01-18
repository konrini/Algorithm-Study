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
		int test = Integer.parseInt(br.readLine());
		for (int i = 1; i <= test; ++i) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			long num1 = Integer.parseInt(st.nextToken());
			long num2 = Integer.parseInt(st.nextToken());
			long sum = 0;
			long cnt = 0;
			long ans = 0;
			boolean check = true;
			while (check) {
				cnt += 1;
				for (int j = 1; j <= 2; ++j) {
					ans += 1;
					sum += cnt;
					if (sum >= num2 - num1) {
						check = false;
						break;
					}
				}
			}
			bw.write(String.valueOf(ans) + "\n");
			bw.flush();
		}
	}
}