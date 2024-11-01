import java.util.Scanner;

public class Main {
    public static final int MAX_NUM = 1000;
    
    public static int n;
    public static int[][] num = new int[MAX_NUM][MAX_NUM];
    public static int[][] dp = new int[MAX_NUM][MAX_NUM];
    
    public static void initialize() {
        dp[0][0] = num[0][0];
    
        for(int i = 1; i < n; i++)
            dp[i][0] = Math.min(dp[i-1][0], num[i][0]);
    
        for(int j = 1; j < n; j++)
            dp[0][j] = Math.min(dp[0][j-1], num[0][j]);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                num[i][j] = sc.nextInt();

        initialize();

        for(int i = 1; i < n; i++)
            for(int j = 1; j < n; j++)
                dp[i][j] = Math.min(Math.max(dp[i-1][j], dp[i][j-1]), num[i][j]);


        System.out.print(dp[n-1][n-1]);
    }
}