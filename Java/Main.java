public class Main {

    public static void main(String[] args) {
        for (int number = 2; number <= 1000000; number++) {
            if (isPrimary(number)) {
                System.out.println(number);
            }
        }
    }

    public static boolean isPrimary(int number) {
        boolean primary = true;
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                primary = false;
            }
        }
        return primary;
    }
}
