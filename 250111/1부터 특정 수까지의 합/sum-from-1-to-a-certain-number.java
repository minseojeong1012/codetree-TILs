import java.util.Scanner;

public class Main {

    public static int sum = 0;
    public static int total = 0;
    public static int answer = 0;

    public static int calc(int n) {
        for (int i = 1; i <=n; i++) {
            sum += i;
        }
        total = sum/10;
        return total;
    }

    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        answer = calc(n);
        System.out.print(answer);
    }
}