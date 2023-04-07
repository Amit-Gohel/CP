import java.util.*;

public class V76_Digits_Frequency {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int d = sc.nextInt();

        int ans = digits_freq(n, d);

        System.out.println(ans);

        sc.close();
    }

    public static int digits_freq(int n, int d){
        int count = 0;
        while(n>0){
            if(n%10 == d){
                count++;
            }
            n/=10;
        }
        return count;
    }
}