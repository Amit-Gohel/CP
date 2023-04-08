import java.util.*;

public class A6_Reverse_the_array {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[] a = new int[n];

        for(int i = 0; i< n; i++){
            a[i] = sc.nextInt();
        }

        for(int i = 0; i<n/2; i++){
            int temp = a[i];
            a[i] = a[n-i-1];
            a[n-i-1] = temp;
        }

        for(int i = 0; i<n; i++){
            System.out.print(a[i]+ ", ");
        }
        sc.close();
    }
}
