import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        double c = a+b;
        double d = a-b;

        double result = c/d;
        System.out.printf("%.2f", result);
    }
}