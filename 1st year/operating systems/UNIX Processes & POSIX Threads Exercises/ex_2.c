#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdio.h>
#include <sys/wait.h>

void furculita(int a){
    int k = fork();
    if(k<0){
        perror("Unable to create child process!");
        exit(1);
    }

    if(k==0){
        if(a == 0)
            exit(0);
        else{
            furculita(a-1);
            printf("Child: %d\nParent: %d\n\n", getpid(), getppid());
    }

    exit(0);
}
}

int main(){

    int n;
    scanf("%d", &n);

    furculita(n);
    for(int i=0; i<n; i++){
        wait(0);
    }

    return 0;
}
