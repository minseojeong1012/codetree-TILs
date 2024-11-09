import java.util.Scanner;
public class Main {
    public static int n,x =0,y=0;

    public static int[] dx = new int[] {1,0,-1,0};
    public static int[] dy = new int[] {0,-1,0,1};

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.

        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            char cdir = sc.next().charAt(0);
            int dist = sc.nextInt();

            int dir=0;
            if (cdir == 'E') {
                dir = 0;
            } else if (cdir == 'S') {
                dir = 1;
            } else if (cdir == 'W') {
                dir = 2;
            } else if (cdir == 'N') {
                dir = 3;
            }
            x += (dx[dir]*dist);
            y += (dy[dir]*dist);

        }
        System.out.println(x+" "+y);
    }
}