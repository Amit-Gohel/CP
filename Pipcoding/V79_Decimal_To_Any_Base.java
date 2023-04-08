import java.util.*;

public class V79_Decimal_To_Any_Base {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int b = sc.nextInt();

        int ans = 0;
        int power = 0;

        while(n>0){
            ans += (n%b)*Math.pow(10, power);
            n = n / b;
            power++;
        }

        System.out.println(ans);

        sc.close();
    }
}
// video link :- https://youtu.be/lOsmPMihcTM