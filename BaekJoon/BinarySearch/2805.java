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
        StringTokenizer st1 = new StringTokenizer(br.readLine() + " ");
        int N = Integer.parseInt(st1.nextToken());
        int M = Integer.parseInt(st1.nextToken());
        int[] tree = new int[N];
        // 나무 길이 최솟값과 최댓값
        int start = 0;
        int end = 0;
        StringTokenizer st2 = new StringTokenizer(br.readLine() + " ");
        // 나무 길이 저장하기
        for (int i = 0; i < N; i++) {
            tree[i] = Integer.parseInt(st2.nextToken());
            if (tree[i] > end) {
                end = tree[i];
            }
        }
        int mid = 0;
        while (start < end) {
            mid = (start + end) / 2;
            // 나무 자르기
            long sum = 0;
            for (int i = 0; i < tree.length; i++) {
                sum += Math.max(tree[i] - mid, 0);
            }
            // 나무가 투머치이므로 길이를 길게 잘라야 한다.
            if (sum >= M) {
                start = mid + 1;
            }
            // 나무가 더 필요하므로 길이를 짧게 잘라야 한다. 
            else {
                end = mid;
            }
        }
        // 최대 높이로 자르고 싶으므로
        bw.write(start - 1 + "");
        bw.close();
    }
}
