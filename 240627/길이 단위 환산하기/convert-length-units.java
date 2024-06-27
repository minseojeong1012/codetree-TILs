import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = sc.nextDouble();
        double aa = 30.48 * a;
        System.out.printf("%.1f",aa);
    }
}