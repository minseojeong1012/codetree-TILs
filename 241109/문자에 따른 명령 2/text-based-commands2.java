import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        String str = sc.next();

        int x = 0;
        int y = 0;

        int currentDir = 0;

        int[] dx = new int[]{0,1,0,-1};
        int[] dy = new int[]{1,0,-1,0};

        for (int i = 0; i < str.length();i++) {
            char cdir = str.charAt(i);

            if (cdir == 'L') {
                currentDir = (currentDir - 1 + 4)%4;
            } else if (cdir == 'R') {
                currentDir = (currentDir + 1)%4;
            } else {
                x += dx[currentDir];
                y += dy[currentDir];
            }
        }
        System.out.println(x+" "+y);
        
    }
}