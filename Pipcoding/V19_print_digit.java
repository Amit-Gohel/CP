import java.util.*;

public class V19_print_digit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int dummy = n;
        int count = 0;
        while(dummy/10 != 0){
            dummy = dummy / 10;
            count++;
        }

        int div = (int) Math.pow(10, count);

        while (div != 0) {
            System.out.println(n / div);
            n = n % div;
            div = div / 10;
        }

        sc.close();
    }
}
