import java.util.Scanner;

public class Main {
    public static final int MAX_N = 1000;

    public static int n;
    public static int[] arr = new int[MAX_N];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int ans = 0;
        int cnt = 0;
        for(int i = 0; i < n; i++) {
            // Case 1
            if(i >= 1 && arr[i] == arr[i - 1])
                cnt++;
            // Case 2
            else
                cnt = 1;
            
            ans = Math.max(ans, cnt);
        }
        
        System.out.print(ans);
    }
}