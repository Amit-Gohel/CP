import java.util.*;

public class V29_Prime_Factorization {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();

        for(int div = 2; div * div <= n; div++){
            while(n % div==0){
                System.out.println(div);
                n /= div;
            }
        }

        if (n != 1) {
            System.out.println(n);
        }
        sc.close();
    }
}
