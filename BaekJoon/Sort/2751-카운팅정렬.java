import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		// 숫자 받기
		int[] arr = new int[N];
		int max = 0;
		int min = 0;
		for (int i = 0; i < N; ++i) {
			arr[i] = sc.nextInt();
			if (arr[i] > max) {
				max = arr[i];
			}
			if (arr[i] < min) {
				min = arr[i];
			}
		}
		// 빈도수 세기
		int[] count = new int[max + Math.abs(min) + 1];
		for (int j = 0; j < N; ++j) {
			++count[arr[j] + Math.abs(min)];
		}
		// 누적 합
		for (int k = 1; k < count.length; ++k) {
			count[k] += count[k - 1];
		}
		// 정렬된 배열
		int[] sorted = new int[N];
		for (int tar = N - 1; tar >= 0; --tar) {
			sorted[--count[arr[tar] + Math.abs(min)]] = arr[tar];
		}
		// 출력
		StringBuilder sb = new StringBuilder();
		for (int n = 0; n < N; ++n) {
			sb.append(sorted[n]).append("\n");
		}
		System.out.println(sb);
	}
}