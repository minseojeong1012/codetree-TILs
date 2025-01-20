import java.util.*;

public class Main {
	
	public static int x, y, n;
	
	public static int[] dx = new int[] {1,-1,0,0};
	public static int[] dy = new int[] {0,0,-1,1};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		
		while(n-- > 0) {
			char cdir = sc.next().charAt(0);
			int dist = sc.nextInt();
			
			int dir;
			if (cdir == 'N') {
				dir = 3;
			} else if (cdir == 'W') {
				dir = 1;
			} else if (cdir == 'E') {
				dir = 0;
			} else {
				dir = 2;
			}
			
			x += dx[dir] * dist;
			y += dy[dir] * dist;
		}
		System.out.print(x + " " + y);
	}

}