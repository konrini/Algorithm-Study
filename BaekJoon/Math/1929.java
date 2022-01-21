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
		int num1 = Integer.parseInt(st.nextToken());
		int num2 = Integer.parseInt(st.nextToken());
		for (int i = num1; i <= num2; ++i) {
			boolean check = true;
			for (int j = 2; j <= Math.sqrt(i); ++j) {
				if (i % j == 0) {
					check = false;
					break;
				}
			}
			if (i == 1) {
				check = false;
			}
			if (check == true) {
				bw.write(i + "\n");
				bw.flush();
			}
		}
	}
}