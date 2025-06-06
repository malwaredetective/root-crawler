#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const char* quotes[] = {
    "Hacking is not a crime. It\'s a skill set.",
    "The quieter you become, the more you can hear.",
    "There is no patch for human stupidity.",
    "I hack, therefore I am.",
    "Knowledge, like air, is vital to life. Like air, no one should be denied it."
};

int main() {
    srand(time(NULL) ^ getpid());
    int idx = rand() % 5;
    puts(quotes[idx]);
    return 0;
}