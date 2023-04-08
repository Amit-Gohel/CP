import java.util.*;

public class V81_Any_base_to_decimal {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int b = sc.nextInt();
        int ans = 0;
        int p = 1;

        while(n>0){
            ans += (n%10)*p;
            n = n/10;
            p*=b;
        }

        System.out.println(ans);
        sc.close();
    }
}
