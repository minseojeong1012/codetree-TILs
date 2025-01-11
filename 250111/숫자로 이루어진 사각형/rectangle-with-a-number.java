import java.util.Scanner;

public class Main {

    public static int count = 1;

    public static void makeSquare(int n) {
        for (int i = 0; i< n; i++) {
            for (int j = 0; j<n ; j++) {
                System.out.print(count+" ");
                count++;
                if (count > 9) {
                    count = 1;
                }
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        makeSquare(n);
    }
}