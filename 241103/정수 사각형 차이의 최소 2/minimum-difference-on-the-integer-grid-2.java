import java.util.Scanner;

public class Main {
    public static final int INT_MAX = Integer.MAX_VALUE;
    public static final int MAX_R = 100;
    public static final int MAX_N = 100;
    
    public static int n;
    public static int[][] num = new int[MAX_N][MAX_N];
    public static int[][] dp = new int[MAX_N][MAX_N];
    
    public static int ans = INT_MAX;
    
    public static void initialize() {
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                dp[i][j] = INT_MAX;
    
        dp[0][0] = num[0][0];
    
        for(int i = 1; i < n; i++)
            dp[i][0] = Math.max(dp[i - 1][0], num[i][0]);
    
        for(int j = 1; j < n; j++)
            dp[0][j] = Math.max(dp[0][j - 1], num[0][j]);
    }
    
    public static int solve(int lowerBound) {

        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                if(num[i][j] < lowerBound)
                    num[i][j] = INT_MAX;
        
        initialize();
    

        for(int i = 1; i < n; i++)
            for(int j = 1; j < n; j++)
                dp[i][j] = Math.max(
                    Math.min(dp[i - 1][j], dp[i][j - 1]), 
                    num[i][j]
                );
            
        return dp[n - 1][n - 1];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        n = sc.nextInt();

        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                num[i][j] = sc.nextInt();


        for(int lowerBound = 1; lowerBound <= MAX_R; lowerBound++) {
            int upperBound = solve(lowerBound);
            
      
            if(upperBound == INT_MAX)
                continue;
            
            ans = Math.min(ans, upperBound - lowerBound);
        }

        System.out.print(ans);
    }
}