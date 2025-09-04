#include <stdio.h>
#include <math.h>

unsigned int isPrimary(unsigned int number) {
    int primary = 1;
    for (unsigned int i = 2; i <= (unsigned int) sqrt(number); i++) {
        if (number % i == 0) {
            primary = 0;
        }
    }
    return primary;
}

int main() {
    for (unsigned int number = 2; number <= 1000000; number++) {
        if (isPrimary(number)) {
            printf("%u\n", number);
        }
    }
    return 0;
}
