import java.util.*;

public class Main {
	
	public static String dirs;
	public static int x, y;
	
	
	public static int dirNum = 3;
	
	public static int[] dx = new int[] {1,0,-1,0};
	public static int[] dy = new int[] {0,-1,0,1};

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		dirs = sc.next();
		
		for (int i = 0; i < dirs.length(); i++) {
			char cdir = dirs.charAt(i);
			
			if(cdir == 'R') {
				dirNum = (dirNum + 1) % 4;
			} else if (cdir == 'L') {
				dirNum = (dirNum - 1 + 4) % 4;
			} else {
				x += dx[dirNum];
				y += dy[dirNum];
			}
		}
		System.out.print(x + " " + y);
	}

}
