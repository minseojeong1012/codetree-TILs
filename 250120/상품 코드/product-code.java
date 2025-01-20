import java.util.*;

class Product {
    public String name;
    public int code;

    public Product() {
        this.name = "codetree";
        this.code = 50;
    }

    public Product(String name, int code) {
        this.name = name;
        this.code = code;
    }
}


public class Main {

    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);

        Product a = new Product();
        Product b = new Product();

        b.name = sc.next();
        b.code = sc.nextInt();

        System.out.println("product " + a.code + " is " + a.name);
        System.out.println("product " + b.code + " is " + b.name);
        
        

    }
}