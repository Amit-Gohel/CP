import java.util.*;

public class V71_Pattern_19 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            if(i==0){
                for(int j = 0; j<n; j++){
                    if(j<=n/2 || j == n-1){
                        System.out.print("* ");
                    }
                    else{
                        System.out.print("  ");
                    }      
                }
            }
            else if(i<n/2){
                for(int j = 0; j<n; j++){
                    if(j==n/2 || j==n-1){
                        System.out.print("* ");
                    }
                    else{
                        System.out.print("  ");
                    }
                }
            }
            else if(i==n/2){
                for(int j = 0; j<n; j++){
                    System.out.print("* ");
                }
            }
            else if(i==n-1){
                for (int j = 0; j < n; j++) {
                    if (j >= n / 2 || j == 0) {
                        System.out.print("* ");
                    } else {
                        System.out.print("  ");
                    }
                }
            }
            else{
                for(int j = 0; j<n;j++){
                    if(j==0 || j==n/2){
                        System.out.print("* ");
                    }
                    else{
                        System.out.print("  ");
                    }
                }
            }
            System.out.println();
        }

        sc.close();
    }
}
