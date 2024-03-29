import java.util.*;

public class V65_Pattern_16 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();

        for(int i = 1; i <= n ; i++){
            for(int j = 1; j <= i; j++){
                System.out.print(j+" ");
            }
            for(int j = 2 * (n - i -1); j >= 0; j--){
                System.out.print("  ");
            }
            for(int j = (n==i) ? i -1 : i ; j > 0; j--){
                System.out.print(j + " ");
            }
            System.out.println();
        }

        sc.close();
    }
}