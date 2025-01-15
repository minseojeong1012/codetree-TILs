import java.util.Scanner;

public class Main {

    public static final int max_n = 100;

    public static int n1, n2;
    public static int[] a = new int[max_n];
    public static int[] b = new int[max_n];


    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();

        for (int i = 0; i<n1;i++) {
            a[i] = sc.nextInt();
        }

        for (int i = 0; i < n2; i++) {
            b[i] = sc.nextInt();
        }

        boolean subSequene = false;

        for (int i = 0; i < n1-n2; i++) {

            boolean isMatch = true;
            
            for (int j = 0; j <n2; j++) {
                
                if (a[i+j] != b[j]) {
                    isMatch = false;
                    break;
                }
            }
            if (isMatch) {
                subSequene = true;
                break;
            }
        }
        if (subSequene) {
            System.out.print("Yes");
        } else {
            System.out.print("No");
        }
    }
}