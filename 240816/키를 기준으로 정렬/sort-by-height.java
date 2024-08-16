import java.util.*;
class Person implements Comparable<Person> {
    String name;
    int length;
    int weight;

    public Person(String name, int length, int weight){
        this.name = name;
        this.length = length;
        this.weight = weight;
    }

    @Override
    public int compareTo(Person person){
        if(this.length > person.length){
            return 1;
        }else if(this.length < person.length){
            return -1;
        }else{
            return 0;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc= new Scanner(System.in);
        int n = sc.nextInt();
        Person[] arr = new Person[n];
        for(int i = 0 ; i < n; i++){
            String name = sc.next();
            int length = sc.nextInt();
            int weight = sc.nextInt();
            arr[i] = new Person(name, length, weight);
        }
        Arrays.sort(arr);
for(int i = 0 ; i < n; i++){
            System.out.println(arr[i].name + " " + arr[i].length + " " + arr[i].weight + " " );
        }
    }
}