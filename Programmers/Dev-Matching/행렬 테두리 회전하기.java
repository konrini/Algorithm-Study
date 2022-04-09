class Solution {
    static int[][] num;
    
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        num = new int[rows][columns];
        for (int i = 0; i < rows; ++i){
            for (int j = 0; j < columns; ++j){
                num[i][j] = i * columns + j + 1;
            }
        }
        for (int cases = 0; cases < queries.length; ++cases) {
            answer[cases] = rotate(queries[cases]);
        }
        return answer;
    }
    
    public static int rotate(int[] query) {
        int r1 = query[0];
        int c1 = query[1];
        int r2 = query[2];
        int c2 = query[3];
        int min = Integer.MAX_VALUE;
        // 왼 -> 오
        int temp_before = num[r1-1][c1-1];
        int temp_save = Integer.MAX_VALUE;
        for (int c = c1-1; c <= c2-1; ++c) {
            if (c == c1-1) {
                temp_before = num[r1-1][c];
                num[r1-1][c] = num[r1][c];
            }
            else {
                temp_save = num[r1-1][c];
                num[r1-1][c] = temp_before;
                temp_before = temp_save;
            }
            if (temp_before < min) {
                min = temp_before;
            }
        }
        // 위 -> 아래
        for (int r = r1; r <= r2-1; ++r) {
            temp_save = num[r][c2-1];
            num[r][c2-1] = temp_before;
            temp_before = temp_save;
            if (temp_before < min) {
                min = temp_before;
            }
        }
        // 오 -> 왼
        for (int c = c2-2; c >= c1-1; --c) {
            temp_save = num[r2-1][c];
            num[r2-1][c] = temp_before;
            temp_before = temp_save;
            if (temp_before < min) {
                min = temp_before;
            }
        }
        // 아래 -> 위
        for (int r = r2-2; r >= r1; --r) {
            temp_save = num[r][c1-1];
            num[r][c1-1] = temp_before;
            temp_before = temp_save;
            if (temp_before < min) {
                min = temp_before;
            }
        }
        return min;
    }
}