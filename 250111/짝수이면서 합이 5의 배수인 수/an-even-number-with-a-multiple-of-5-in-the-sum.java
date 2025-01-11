import java.util.Scanner;

public class Main {

    public static int sum = 0;

    public static boolean isMagicnumber(int n) {
        sum = (n/10) + (n%10);

        return n%2==0 && sum%5==0; 
    }

    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if (isMagicnumber(n)) {
            System.out.print("Yes");
        } else {
            System.out.print("No");
        }
    }
}