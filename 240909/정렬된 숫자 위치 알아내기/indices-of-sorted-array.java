import java.util.Scanner;
import java.util.Arrays;
import java.util.Comparator;

class Num implements Comparable<Num>{
    int value;
    int originIdx;// 원래 입력받은 위치
    int newIdx; // 정렬 후의 이동된 위치를 새로 저장한다

    public Num(int value, int originIdx){
        this.value = value;
        this.originIdx = originIdx;
    }

    // 오름차순 정렬
    public int compareTo(Num num){
        return this.value - num.value;
    }
    
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Num[] numbers = new Num[n];

        for(int i = 0; i < n; i++){
            int num = sc.nextInt();
            numbers[i] = new Num(num, i);
        }

        Arrays.sort(numbers);

        for(int i = 0; i < n; i++){
            numbers[i].newIdx = i + 1;
        }

        // 원래 인덱스의 오름차순으로 다시 정렬하기
        Arrays.sort(numbers, new Comparator<Num>() {
            @Override
            public int compare(Num a, Num b){
                return a.originIdx - b.originIdx;
            }
        });

        for(int i = 0; i < n; i++){
            System.out.print(numbers[i].newIdx + " ");
        }

        
    }
}