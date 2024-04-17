import java.util.*;
import java.time.*;
import java.time.temporal.ChronoUnit;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.nextLine(); 

        Weather[] weathers = new Weather[n];

        for (int i = 0; i < weathers.length; i++) {
            LocalDate date = LocalDate.parse(sc.next());
            String day = sc.next();
            String state = sc.next();

            weathers[i] = new Weather(date, day, state);
        }
        
        Weather[] rainyWeathers = Arrays.stream(weathers)
            .filter(w -> "Rain".equals(w.state))
            .toArray(Weather[]::new);

        Arrays.sort(rainyWeathers, Comparator.comparing(weather -> weather.date));

        System.out.print(rainyWeathers[0]);        
    }
}

class Weather {
    LocalDate date;
    String day;
    String state;

    public Weather(LocalDate date, String day, String state) {
        this.date = date;
        this.day = day;
        this.state = state;
    }

    public String toString() {
        return date + " " + day + " " + state;
    }
}