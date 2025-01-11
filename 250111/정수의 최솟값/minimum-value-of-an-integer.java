import java.util.Scanner;

public class Main {

    public static int answer = 0;

    public static int findMin(int a, int b) {
        answer = Math.min(a,b);
        return(answer);
    }

    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        System.out.print(findMin(a,findMin(b,c)));
    }
}