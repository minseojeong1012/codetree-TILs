import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int y = sc.nextInt();
        int m = sc.nextInt();
        int d = sc.nextInt();

        if(!isExistDay(y,m,d)) {
            System.out.print("-1");
            System.exit(0);
        }
        
        if(3 <=m && m <=5) {
            System.out.print("Spring");
        }
        else if (6<=m && m <= 8) {
            System.out.print("Summer");
        }
        else if ( 9<=m && m <= 11) {
            System.out.print("Fall");
        }
        else {
            System.out.print("Winter");
        }

    }

    public static boolean isLeapYear(int y) {
        //4의 배수가 아니라면 윤년이 확실히 아님
        if (y%4 !=0)
            return false;
        //4의 배수가 아닌 수 중 100의 배수가 아니라면 윤년
        if (y%100 != 0)
            return true;
        //위 조건을 지난 수 중 400의 배수라면 윤년
        if (y%400 == 0)
            return true;
        //여기까지 온 수는 100의 배수이지만, 400의 배수가 아니므로 윤년이 아님    
        return false;
    }

    public static boolean isExistDay(int y, int m, int d) {
        int [] numOfDays = new int[]{0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        //윤년 처리
        numOfDays[2] = isLeapYear(y) ? 29:28;

        //d가 해당월의 최대 일 수를 넘지 않아야 합니다.
        return d <= numOfDays[m];
    }

}