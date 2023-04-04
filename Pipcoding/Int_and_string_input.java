import java.util.*;

public class Int_and_string_input {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // In program when we use int and string both as input at that time we have to
        // use below code other vise program will not run appropriate

        // Wrong code which not run appropriate
        int a = sc.nextInt();
        String name = sc.nextLine();

        // right code
        // int a = Integer.parseInt(sc.nextLine());
        // String name = sc.nextLine();

        System.out.println(a);
        System.out.println(name);

        sc.close();
    }
}
