import java.util.Scanner;

public class Main {

    public static int sum = 0;

    public static boolean findNum(int num) {
        if (num == 1) {
            return false;
        }
        for (int i = 2; i < num-1; i++) {
            if (num % i == 0){
                return false;
            }
        }
        return true;
        
    }

    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        for (int i = a; i<=b; i++) {
            if (findNum(i)) {
                sum +=i;
            }
        }
        System.out.print(sum);
    }
}