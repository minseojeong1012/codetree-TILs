import java.util.Scanner;

public class Main {

    public static boolean findNum(int n) {
        return insIncluded(n) || (n%3 ==0);
    }

    public static boolean insIncluded(int n) {
        while (n>0) {
            if (n % 10 == 3 || n % 10 == 6 || n % 10 == 9) {
                return true;
            }
            n/=  10;
        }
        return false;
    }

    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        int cnt = 0;
        
        for (int i = a; i <= b; i++) {
            if (findNum(i)) {
                cnt++;
            }
        }
        System.out.print(cnt);
    }
}
