import java.util.Scanner;
public class Main {

    public static final int OFFSET = 100;

    public static int[] x1 = new int[100];
    public static int[] x2 = new int[100];

    public static int[] checked = new int[200+1];

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i<n;i++) {
            x1[i] = sc.nextInt();
            x2[i] = sc.nextInt();

            x1[i] += 100;
            x2[i] += 100;
        }

        for(int i = 0; i < n; i++) {
            for (int j = x1[i]; j <x2[i]; j++) {
                checked[j]++; 
            }
        }

        int max = 0;
        for (int i = 0; i<=200; i++) {
            if(checked[i]>max) {
                max = checked[i];
            }
        }
        System.out.print(max);


    }
}