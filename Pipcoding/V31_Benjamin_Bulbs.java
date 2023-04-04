import java.util.*;

public class V31_Benjamin_Bulbs {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for(int div = 1; div * div <= n; div++){
            System.out.println(div*div);
        }

        sc.close();
    }
}
