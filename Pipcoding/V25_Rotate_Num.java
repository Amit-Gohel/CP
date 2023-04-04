import java.util.*;

public class V25_Rotate_Num {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int num = sc.nextInt();
        int rotate = sc.nextInt();
        int digit_num = count(num);

        rotate %= digit_num;
        if(rotate < 0){
            rotate += digit_num;
        }

        while(rotate>0){
            // get first postion of the number
            int first_pos = num/(int)Math.pow(10, digit_num-1);
            // remove first postion of the number
            num -=  first_pos*(int)Math.pow(10, digit_num-1);
            // adding to first postion number to last position 
            num *= 10;
            num += first_pos;
            rotate--;
        }

        System.out.println(num);
        sc.close();
    }

    // return the tital digit number
    public static int count(int n){
        int count = 0;
        while(n>0){
            n/=10;
            count++;
        }
        return count;
    }
}
