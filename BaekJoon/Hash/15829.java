import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int L = Integer.parseInt(br.readLine());
		String str = br.readLine();
		double hash = 0;
		double right = (double) 1/31;
		for (int i = 0; i < L; ++i) {
			right *= 31;
			if (right >= 1234567891) {
				right = right % 1234567891;
			}
			hash += ((str.charAt(i) - 'a' + 1) * right);
		}
		hash %= 1234567891;
		bw.write((int) hash + "");
		bw.close();
	}
}