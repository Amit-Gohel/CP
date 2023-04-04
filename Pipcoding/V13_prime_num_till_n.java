import java.util.*;

public class V13_prime_num_till_n {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int low = sc.nextInt();
        int high = sc.nextInt();

        sc.close();

        for(; low<=high; low++){
            int count = 0;
            for(int div = 2; div*div <= low; div++ ){
                if(low%div == 0){
                    count++;
                    break;
                }
            }
            if(count == 0){
                System.out.println(low);
            }
        }
    }
}
