#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const char* quotes[] = {
    "A true hacker sees failure not as defeat, but as data.",
    "The quieter you become, the more you are able to hear.",
    "The world isn’t run by weapons anymore, or energy, or money. It’s run by little ones and zeroes, little bits of data.",
    "The best defense is a good offense.",
    "If you can't find a way, create one."
};

int main() {
    srand(time(NULL) ^ getpid());
    int idx = rand() % 5;
    puts(quotes[idx]);
    return 0;
}