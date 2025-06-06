#include <stdio.h>
#include <stdlib.h>
#include <dlfcn.h>

int main() {
    printf("Cyber Security Assistant: Starting a vulnerability scan on your localhost ...\n");
    void *handle = dlopen("libscan.so", RTLD_NOW);
    if (!handle) {
        fprintf(stderr, "Error loading a shared library: %s\n", dlerror());
        return 1;
    }
    void (*scan)() = dlsym(handle, "scan");
    if (!scan) {
        fprintf(stderr, "Error finding scan(): %s\n", dlerror());
        dlclose(handle);
        return 1;
    }
    scan();
    dlclose(handle);
    printf("The scan completed successfully!\n");
    return 0;
}
