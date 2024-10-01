import java.util.Scanner;
public class Main {

    public static final int MAX_N = 100;

    public static int[] arr = new int[MAX_N+1];


    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int m = sc.nextInt();

        for (int i = 1; i<= n ;i++) {
            arr[i] = sc.nextInt();
        }


        for (int i = 0; i < m; i++) {
            int total = 0;
            int a = sc.nextInt();
            int b = sc.nextInt();
            int finalValue = addUp(arr, a,b);
            System.out.println(finalValue);
            
        }
    }

    public static int addUp(int[] arr,int a, int b) {
        int sum = 0;
        for (int i = a; i<=b; i++) {
            sum += arr[i];
        }
        return sum;
    }
}