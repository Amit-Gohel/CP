import java.util.*;

public class V23_inverse_num {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int out_num = 0;
        int temp;
        int count = 1;

        while (n > 0) {
            temp = n%10;
            out_num += count*(int)Math.pow(10, temp - 1);
            n = n / 10;
            count++;
        }
        System.out.println(out_num);

        sc.close();
    }
}
