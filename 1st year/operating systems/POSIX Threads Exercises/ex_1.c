#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <pthread.h>
#include <sys/wait.h>

int main(){
    int n, p;
    scanf("%d", &n);

    for(int i=0; i<n; i++){
        p = fork();

        if(p<0){
            perror("Unable to create child process!");
            exit(1);
        }

        if(p==0){
            printf("Child: %d\nParent: %d\n\n", getpid(), getppid());
            exit(0);
        }

        wait(0);
        }
    return 0;
}
