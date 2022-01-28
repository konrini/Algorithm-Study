import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String str = br.readLine().toUpperCase();
		int[] cnt = new int[26];
		for (int i = 0; i < str.length(); ++i) {
			cnt[str.charAt(i) - 'A'] += 1;
		}
		int idx = 0;
		int max = 0;
		int check = 1;
		for (int j = 0; j < cnt.length; ++j) {
			if (cnt[j] == max) {
				check += 1;
			} else if (cnt[j] > max) {
				max = cnt[j];
				idx = j;
				check = 1;
			}
		}
		if (check > 1) {
			bw.write("?");
		} else {
			bw.write((char) ('A' + idx));
		}
		bw.close();
	}
}