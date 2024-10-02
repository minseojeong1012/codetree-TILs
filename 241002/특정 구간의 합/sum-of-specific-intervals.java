import java.util.Scanner;

public class Main {

    public static final int maxNumber = 100;

    public static int[] arr = new int[maxNumber+1];


    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 1; i<= m; i++) {
            int sum = 0;
            int a = sc.nextInt();
            int b = sc.nextInt();
            int result = addUp(a,b);
            System.out.println(result);
        }
    }
    public static int addUp(int a , int b) {
        int total = 0;
        for (int i = a; i<=b;i++) {
            total += arr[i];
        }
        return total;
    }
    
}