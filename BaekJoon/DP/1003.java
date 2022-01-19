import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int test = Integer.parseInt(br.readLine());
		for (int i = 0; i < test; ++i) {
			int target = Integer.parseInt(br.readLine());
			int[] cntone = new int[41];
			int[] cntzero = new int[41];
			cntone[0] = 0;
			cntzero[0] = 1;
			cntone[1] = 1;
			cntzero[1] = 0;
			for (int idx = 2; idx <= target; ++idx) {
				cntone[idx] = cntone[idx - 1] + cntone[idx - 2];
				cntzero[idx] = cntzero[idx - 1] + cntzero[idx - 2];
			}
			bw.write(String.valueOf(cntzero[target] + " " + cntone[target] + "\n"));
			bw.flush();
		}
	}
}
