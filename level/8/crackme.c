#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define KEY 0x55

// Obfuscated Flag
unsigned char flag_obf[] = {
    0x33, 0x39, 0x34, 0x32, 0x2e, 0x12, 0x17, 0x11, 0xa, 0x38, 0x30, 0xa, 0x36, 0x27, 0x34, 0x2f, 0x2c, 0xa, 0x22, 0x3c, 0x21, 0x3d, 0xa, 0x21, 0x3d, 0x3a, 0x26, 0x30, 0xa, 0x26, 0x3e, 0x3c, 0x39, 0x39, 0x26, 0x28, 0x00
}; 
size_t flag_len = 0;

void print_flag() {
    unsigned char real_flag[64];
    for (size_t i = 0; flag_obf[i]; ++i) {
        real_flag[i] = flag_obf[i] ^ KEY;
        flag_len = i+1;
    }
    real_flag[flag_len] = '\0';
    printf("Congratulations! Here is your flag:\n%s\n", real_flag);
}

int main() {
    char buf[64];
    unsigned char pass_obf[] = { 'd'^KEY, 'e'^KEY, 'b'^KEY, 'u'^KEY, 'g'^KEY, 'm'^KEY, 'e'^KEY, 0 };
    char password[16];
    for (int i=0; i<7; i++) password[i] = pass_obf[i] ^ KEY;
    password[7] = 0;

    printf("Enter password: ");
    fflush(stdout);
    if (!fgets(buf, sizeof(buf), stdin)) {
        puts("Error reading input.");
        return 1;
    }
    buf[strcspn(buf, "\n")] = 0;

    if (strcmp(buf, password) == 0) {
        print_flag();
    } else {
        puts("Wrong password.");
    }
    return 0;
}
