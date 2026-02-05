import java.util.ArrayList;
import java.util.List;

public class Prime {
    public static void main(String[] args) {
        List<Integer> primes = new ArrayList<>();
        int x = 1;
        int y = 100;

        for (int i = 2; i <= y; i++) {
            boolean isPrime = true;

            for (int j = 2; j <= i / 2; j++) {
                if (i % j == 0) {
                    isPrime = false; 
                    break;           
                }
            }

            if (isPrime) {
                primes.add(i);
            }
        }
        
        System.out.println("Prime numbers between " + x + " and " + y + ":");
        System.out.println(primes);
    }
}