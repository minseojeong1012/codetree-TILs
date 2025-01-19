import java.util.*;

class Answer {
    String secretCode;
    char meetingPoint;
    int time;

    public Answer(String secretCode, char meetingPoint, int time) {
        this.secretCode = secretCode;
        this.meetingPoint = meetingPoint;
        this.time = time;
    }
};


public class Main {

    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        String sCode;
        char mPoint;
        int time;

        sCode = sc.next();
        mPoint = sc.next().charAt(0);
        time = sc.nextInt();

        Answer answer = new Answer(sCode, mPoint, time);

        System.out.println("secret code : " + answer.secretCode);
        System.out.println("meeting point : " + answer.meetingPoint);
        System.out.println("time : " + answer.time);

    }
}