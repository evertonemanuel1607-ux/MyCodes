import java.util.Scanner;;

class IfElse {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Number: ");
        int number = scanner.nextInt();
        if (number > 5) {
            System.out.println("is than bigger 5");
        }
        else {
            System.out.println("Is not than bigger 5");
        }
        scanner.close();
    }
}