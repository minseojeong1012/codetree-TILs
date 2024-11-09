import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);

        int x = 0;
        int y = 0;

        int currentdir = 0;

        int[] dx = new int[]{0,1,0,-1};
        int[] dy = new int[]{1,0,-1,0};

        String str = sc.next();

        for (int i = 0; i < str.length();i++) {
            char cdir = str.charAt(i);

            if (cdir == 'R') {
                currentdir = (currentdir + 1) % 4;
            } else if (cdir == 'L') {
                currentdir = (currentdir - 1 + 4) %4;
            } else {
                x += dx[currentdir];
                y += dy[currentdir];
            }
        }
        System.out.println(x+" "+y);
        
    }
}