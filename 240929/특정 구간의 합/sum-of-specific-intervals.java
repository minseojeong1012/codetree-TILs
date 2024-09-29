import java.util.Scanner;

public class Main {
    public static final int MAX_N = 100;

    public static int[] arr = new int[MAX_N+1];
    public static int cnt;

    public static int getAnswer(int a1, int a2) {
        int returnValue = 0;
        for (int i = a1; i <=a2; i++) {
            returnValue += arr[i];
        }
        return returnValue;
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        for (int i = 1; i <=n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 1; i <=m; i++) {
            int a1 = sc.nextInt();
            int a2 = sc.nextInt();
            System.out.println(getAnswer(a1,a2));
        }


    }
}