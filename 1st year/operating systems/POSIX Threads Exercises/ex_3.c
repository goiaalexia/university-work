#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/time.h>
#include <sys/wait.h>

int main(int argc, char* argv[]){
    struct timeval tv1, tv2;
    int f = fork();
    if(f<0){
        perror("Unable to fork!");
        exit(1);
    }
    else if(f==0){
        if(argc<2){
            perror("Not enough arguments!");
            exit(2);
        }
    gettimeofday(&tv2, NULL);
    if(execvp(argv[1], argv+1) == -1){
        perror("Error running command!");
        exit(3);
    } else{exit(0);}
    }
    else{
    wait(0);
    gettimeofday(&tv1, NULL);
    printf("Executed in %d time.", (int)(tv1.tv_sec-tv2.tv_sec));
    return 0;
}}
