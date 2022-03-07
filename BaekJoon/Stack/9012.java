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
			List<Character> stack = new ArrayList<>();
			String str = br.readLine();
			String ans = "YES";
			for (int j = 0; j < str.length(); ++j) {
				if (str.charAt(j) == '(') {
					stack.add(str.charAt(j));
				} else {
					if (stack.size() == 0) {
						ans = "NO";
						break;
					} else {
						stack.remove(stack.size() - 1);
					}
				}
			}
			if (stack.size() > 0) {
				ans = "NO";
			}
			bw.write(ans + "\n");
		}
		bw.flush();

	}
}
