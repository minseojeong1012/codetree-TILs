import java.util.*;
public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        //원소의 개수
        int n = sc.nextInt();

        int[] arr = new int[n];
        int[] arr2 = new int[n];

        for (int i = 0; i< n; i++) {
            arr[i] = sc.nextInt();
        }
        //arr 정렬
        Arrays.sort(arr);
        // for (int i = 0; i< n; i++) {
        //     System.out.print(arr[i]);
        // }

        for (int i = 0; i< n; i++) {
            arr2[i] = sc.nextInt();
        }
        //arr2 정렬
        Arrays.sort(arr2);
        // for (int i = 0; i< n; i++) {
        //     System.out.print(arr2[i]);
        // }


        boolean isMatch = true;
        for (int i = 0; i < n ; i++) {
            if (arr[i] != arr2[i]) {
                isMatch = false;
            }
        }

        if (isMatch) {
            System.out.print("Yes");
        } else {
            System.out.print("No");
        }

    }
}