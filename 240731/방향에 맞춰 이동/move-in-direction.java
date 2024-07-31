import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int x = 0, y = 0;

        int[] dx = new int[]{1,0,-1,0};
        int[] dy = new int[]{0,-1,0,1};
        int nx, ny;

        for(int i = 0; i < n;i++) {
            char way = sc.next().charAt(0);
            int dist = sc.nextInt();

            int dir=0;

            if (way == 'E'){
                dir = 0;
            } 
            else if (way == 'N') {
                dir = 3;
            }
            else if (way == 'S') {
                dir = 1;
            }
            else if (way == 'W') {
                dir = 2;
            }

            x +=dx[dir]*dist;
            y +=dy[dir]*dist;
        }

System.out.print(x+" "+y);
    }
}