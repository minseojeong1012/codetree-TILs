import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int[] dx = new int[]{1,  0, -1, 0};
        int[] dy = new int[]{0, -1,  0, 1};

        int dirNum = 3;
        int x = 0;
        int y = 0;

        String dir = sc.next();

        for (int i = 0; i <dir.length();i++) {
            char cdir = dir.charAt(i);

            if (cdir == 'L') {
                dirNum = (dirNum +3) %4;
            } else if (cdir == 'R') {
                dirNum = (dirNum+1) %4;
            }
            else {
                x += dx[dirNum];
                y += dy[dirNum];
            }
        }

        System.out.print(x+" "+y);


    }
}