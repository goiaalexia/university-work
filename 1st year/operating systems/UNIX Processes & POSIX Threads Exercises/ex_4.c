#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

/*
 *  * G=0
 *   * N threads - alter G
 *    * Main - print the value of G once per 2s 10 times.
 *    */

int G=0;

pthread_mutex_t m=PTHREAD_MUTEX_INITIALIZER;

void* fthread(void* a) {
    int id=*(int*)a;
    free(a);
    printf("Thread %d started.\n", id);
    int i=0;
    while(i<100) {
        printf("Thread %d altering G.\n", id);
        pthread_mutex_lock(&m);
        G+=rand()%10;
        pthread_mutex_unlock(&m);
        sleep(3);
    }
    printf("Thread %d ended.\n", id);
    return NULL;
}

int main(int argc, char **argv) {
    if(argc>1) {
        int n=atoi(argv[1]);
        printf("The number of threads is: %d\n", n);

        pthread_t *th=(pthread_t*)malloc(n*sizeof(pthread_t));

        for(int i=0; i<n; i++) {
            int *p = (int*)malloc(sizeof(int));
            *p = i;
            if(pthread_create(&th[i], NULL, fthread, &p) < 0) {
                perror("Unable to create a thread");
                exit(2);
            }
        }

        int i=0;
        while(i<10) {
 	sleep(2);
            pthread_mutex_lock(&m);
            printf("G: %d\n", G);
            pthread_mutex_unlock(&m);
            i++;
        }


        for(int i=0; i<n; i++) {
            pthread_join(th[i], NULL);
        }
        free(th);
    } else {
        perror("Usage #threads missing.\n");
        exit(1);
    }
    return 0;
}
