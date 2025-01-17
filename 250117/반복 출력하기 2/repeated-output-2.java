import java.util.Scanner;

public class Main {

    public static void printWords(int n) {

        if (n == 0) {
            return;
        }
        printWords(n-1);
        System.out.println("HelloWorld");
    }


    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        printWords(n);
    }
}