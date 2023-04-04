import java.util.*;

public class V21_reverse_num {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        while(n>0){
            System.out.println(n%10);
            n=n/10;
        }

        sc.close();
    }
}
