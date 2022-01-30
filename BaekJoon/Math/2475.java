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
		int total = 0;
		for (int i = 0; i < 5; ++i) {
			int temp = Integer.parseInt(st.nextToken());
			total += Math.pow(temp, 2);
		}
		bw.write(total % 10 + "");
		bw.close();
	}
}