#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>

// Function to check if a string is a valid integer
int is_number(const char *str) {
    if (*str == '-' || *str == '+') str++;
    if (!*str) return 0;
    while (*str) {
        if (!isdigit((unsigned char)*str)) return 0;
        str++;
    }
    return 1;
}

int main(int argc, char *argv[]) {
    int roll, modifier = 0;

    // Seed the random number generator
    srand((unsigned int)time(NULL));

    // Roll the dice (1-20)
    roll = (rand() % 20) + 1;

    if (argc == 2) {
        if (!is_number(argv[1])) {
            printf("Error: Modifier must be an integer.\n");
            return 1;
        }
        modifier = atoi(argv[1]);
        printf("Rolled: %d\n", roll);
        printf("With modifier (%d): %d\n", modifier, roll + modifier);
    } else if (argc == 1) {
        printf("Rolled: %d\n", roll);
    } else {
        printf("Usage: %s [modifier]\n", argv[0]);
        return 1;
    }

    return 0;
}
