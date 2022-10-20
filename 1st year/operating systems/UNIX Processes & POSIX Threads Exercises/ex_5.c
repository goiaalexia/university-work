#include <pthread.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>

int* arrayyy;

pthread_mutex_t* m;

struct Arg{
    char* path;
    int number;
    pthread_cond_t* var;
};


void* f1(void* a){

    struct Arg arg = *(struct Arg*)a;
    //free(a);

    char* filename = (char*)arg.path;
    int no1, no2;
    int i = arg.number;

    FILE* file = fopen(filename, "r");

    fscanf(file, "%d", &no1);
    fscanf(file, "%d", &no2);

    fclose(file);

    while(arrayyy[i]<no2){
        printf("Thread %d adding to the array.\n", i);

        arrayyy[i] += no1;

    }

    //free(filename);
    pthread_cond_signal(arg.var);
    return NULL;
}
void* f2(void* a){
    struct Arg arg = *(struct Arg*)a;
    //free(a);
    int num = arg.number;

    pthread_cond_wait(arg.var, &m[num-1]);

    printf("Thread %d done adding. GLOBAL VARIABLE: %d\n", num, arrayyy[num]);

    return NULL;
}
int main(int argc, char** argv){

    arrayyy = malloc(sizeof(int)*argc); // allocate the n numbers.
    m = malloc(sizeof(pthread_mutex_t)*(argc-1)); // allocate a mutex for each.

    for(int i=0; i<argc-1; i++){
    pthread_mutex_init(&m[i], NULL);
    }

    for(int i=1; i<argc; i++){

        pthread_t x,y;
        pthread_cond_t cd = PTHREAD_COND_INITIALIZER;
        pthread_mutex_lock(&m[i-1]);

        struct Arg pass;
        pass.path = argv[i];
        pass.number = i;
        pass.var = &cd;

        if(pthread_create(&x, NULL, f1, &pass)<0){
            perror("Unable to create thread x!");
            exit(1);
        }

        if(pthread_create(&y, NULL, f2, &pass)<0){
            perror("Unable to create thread x!");
            exit(1);
        }

        pthread_join(x, NULL);
        pthread_join(y, NULL);
    }

    for(int i=0; i<argc-1; i++){
    pthread_mutex_destroy(&m[i]);
    }
    //free(arrayyy);

    return 0;
}

