import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;


public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Queue<Integer> q = new LinkedList<>();
        String str = sc.next();

        for (int i = str.length()-1; i>=0; i--){
            q.add(Integer.parseInt(str.substring(i,i+1)));
        }

        
        int sum = 0;
        int mul = 1;

        while(!q.isEmpty()){
            int num = q.poll();
            sum += num * mul;
            mul *= 2;
            
        }
        System.out.print(sum);


    }
}