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
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st1.nextToken()); // 세로
        int W = Integer.parseInt(st1.nextToken()); // 가로
        int[][] map = new int[H][W];
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i = 0; i < W; i++) {
            int height = Integer.parseInt(st2.nextToken());
            for (int j = 0; j < height; j++) {
                map[j][i] = 1;
            }
        }
        int cnt = 0;
        for (int i = 0; i < H; i++) {
            boolean check = false;
            int temp_cnt = 0;
            for (int j = 0; j < W; j++) {
                if (!check && map[i][j] == 1) {
                    check = true;
                } else if (check && map[i][j] == 0) {
                    ++temp_cnt;
                } else if (check && map[i][j] == 1) {
                    cnt += temp_cnt;
                    temp_cnt = 0;
                }
            }
        }
        bw.write(cnt + "");
        bw.close();
    }
}
