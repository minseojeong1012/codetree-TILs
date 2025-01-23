import java.util.*;

public class Main {
	
	public static int n;
	
	public static int max_n = 100;
	
	public static int[][] arr = new int[max_n][max_n];
	
	public static int[] dx = new int[] {-1,0,1,0};
	public static int[] dy = new int[] {0,1,0,-1};
	
	public static int dir = 4;
	
	
	public static boolean isRange(int x, int y) {
		return (0 <= x && x < 5 && y >= 0 && y < 5);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		
		//n * n 만큼 배열 입력 받기
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if(check(i, j) >= 3) {
					cnt ++;
				}
			}
		}
		System.out.println(cnt);
		
		
	}
	
	
	public static int check(int i, int j ) {
		int number = 0;
		for (int a = 0; a < dir; a++) {
			int nx = i + dx[i];
			int ny = j + dy[i];
			if( isRange(nx, ny) && arr[nx][ny] == 1) {
				number++;
			}
		}
		return number;
	}

}
