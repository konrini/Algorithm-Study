import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    static String[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        arr = new String[N][N];
        star(0, 0, N, false);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                bw.write(arr[i][j]);
            }
            bw.write("\n");
        }
        bw.close();
    }

    public static void star(int r, int c, int size, boolean blank) {
        if (blank) {
            for (int i = r; i < r + size; i++) {
                for (int j = c; j < c + size; j++) {
                    arr[i][j] = " ";
                }
            }
            return;
        }
        if (size == 1) {
            arr[r][c] = "*";
            return;
        }
        int count = 0;
        for (int i = r; i < r + size; i += size / 3) {
            for (int j = c; j < c + size; j += size / 3) {
                count++;
                if (count == 5) {
                    star(i, j, size / 3, true);
                } else {
                    star(i, j, size / 3, false);
                }
            }
        }
    }
}
