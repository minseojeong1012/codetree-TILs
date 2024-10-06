import java.util.Scanner;
public class Main {

    public static final int MAX_N = 100;
    public static final int MAX_K = 100;

    public static int[] a = new int[MAX_K+1];
    public static int[] b = new int[MAX_K+1];

    public static int[] checks = new int[MAX_N+1]; 

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int k = sc.nextInt();

        for (int i = 1; i <=k; i++) {
            a[i] = sc.nextInt();
            b[i] = sc.nextInt();
        }

        for (int i = 1; i<=k; i++) {
            for (int j = a[i]; j<=b[i]; j++) {
                checks[j]++;
            }
        }
        int max = 0;
        for (int i = 0; i<=n;i++) {
            if (checks[i]>max) {
                max = checks[i];
            }
        }
        System.out.print(max);
    }
}