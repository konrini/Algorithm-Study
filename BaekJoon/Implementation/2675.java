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
			int num = Integer.parseInt(st.nextToken());
			String str = st.nextToken();
			String[] characters = str.split("");
			for (int j = 0; j <= characters.length-1; ++j) {
				for (int k = 1; k <= num; ++k) {
					bw.write(characters[j]);
				}
			}
			bw.write("\n");
			bw.flush();
		}
	}
}
