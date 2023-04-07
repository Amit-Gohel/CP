import java.util.*;

public class V67_Pattern_17 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for(int i = 0; i < n; i++){
            for(int j = 0; j <= n/2 - 1; j++){
                if (i == n/2){
                    System.out.print("* ");
                }
                else{
                    System.out.print("  ");
                }
            }
            for(int j = (i > n/2) ? n - i - 1: i; j >= 0; j--){
                System.out.print("* ");
            }
            System.out.println();
        }

        sc.close();
    }
}
