import java.util.Scanner;

public class Main {
    static int a,b;
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int i = sc.nextInt();
        int j = sc.nextInt();
        changeNumber(i,j);
        System.out.print(a+" "+b);



    }

    static void changeNumber(int i, int j) {
        if (i>j) {
            b = j +10;
            a = i*2;
        } else {
            a = i + 10;
            b = j*2;
        }
    }
}