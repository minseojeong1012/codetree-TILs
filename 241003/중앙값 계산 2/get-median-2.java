import java.util.Scanner;
import java.util.Arrays;

public class Main {

    public static int[] arr = new int[100];

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i<n; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i <n; i++) {
            if (i %2 == 0) {
                Arrays.sort(arr,0,i+1);
                System.out.print(arr[i/2]+" ");
            }
        }
    }
}