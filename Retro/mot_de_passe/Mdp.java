package chall;

import java.util.Scanner;
/* loaded from: Mdp.class */
public class Mdp {
    public static void main(String[] strArr) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Mot de passe Admin:");
        if ("4/2@PAu<+ViNgg%^5NS`#J\u001fNK<XNW(_".equals(hide(scanner.nextLine()))) {
            System.out.println("Bienvenue Admin");
        } else {
            System.out.println("Au revoir non admin");
        }
    }

    static String hide(String str) {
        String str2 = "";
        for (int i = 0; i < str.length(); i++) {
            str2 = str2 + ((char) (((char) (str.charAt(i) - i)) % 128));
        }
        return str2;
    }
}
