import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Cell implements Comparable<Cell> {
    int num, x, y;

    public Cell(int num, int x, int y) {
        this.num = num;
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Cell c) {
        return this.num - c.num;
    }
}

public class Main {
    public static final int DIR_NUM = 4;
    public static final int MAX_N = 500;
    
    public static int n;
    public static int[][] grid = new int[MAX_N][MAX_N];
    public static int[][] dp = new int[MAX_N][MAX_N];
    
    public static ArrayList<Cell> cells = new ArrayList<>();
    public static int ans = 0;
    
    public static boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < n;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 입력
        n = sc.nextInt();

        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                grid[i][j] = sc.nextInt();


        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                cells.add(new Cell(grid[i][j], i, j));
        
        Collections.sort(cells);

        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                dp[i][j] = 1;


        for(int i = 0; i < cells.size(); i++) {
            int x = cells.get(i).x;
            int y = cells.get(i).y;
            int[] dx = new int[]{-1, 1,  0, 0};
            int[] dy = new int[]{ 0, 0, -1, 1};

            for(int j = 0; j < DIR_NUM; j++) {
                int nx = x + dx[j], ny = y + dy[j];
                if(inRange(nx, ny) && grid[nx][ny] > grid[x][y])
                    dp[nx][ny] = Math.max(dp[nx][ny], dp[x][y] + 1);
            }
        }

        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                ans = Math.max(ans, dp[i][j]);

        System.out.print(ans);
    }
}