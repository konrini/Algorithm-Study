import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int N = Integer.parseInt(br.readLine());
		Integer[] numbers = new Integer[N];

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			numbers[i] = Integer.parseInt(st.nextToken());
		}

		HashSet<Integer> set = new HashSet<Integer>(Arrays.asList(numbers));
		Integer[] arr = set.toArray(new Integer[0]);
		Arrays.sort(arr);

		Map<Integer, Integer> dict = new HashMap<>();
		for (int j = 0; j < arr.length; j++) {
			dict.put(arr[j], j);
		}

		for (int k = 0; k < N; k++) {
			bw.write(dict.get(numbers[k]) + " ");
		}
		bw.close();
	}
}