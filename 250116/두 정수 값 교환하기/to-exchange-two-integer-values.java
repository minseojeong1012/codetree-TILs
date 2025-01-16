import java.util.Scanner;

class intWrapper {
    int value;

    public intWrapper (int value) {
        this.value = value;
    }
}


public class Main {

    public static void change(intWrapper n, intWrapper m) {
        int temp = n.value;
        n.value = m.value;
        m.value = temp;

    }

    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        intWrapper nWrapper = new intWrapper(n);
        intWrapper mWrapper = new intWrapper(m);

        change(nWrapper,mWrapper);

        n = nWrapper.value;
        m = mWrapper.value;
        System.out.print(n+ " " +m);

    }
}