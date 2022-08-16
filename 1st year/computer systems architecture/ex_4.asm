bits 32 ; assembling for the 32 bits architecture
; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit,printf,scanf; add the external functions that we need
import exit msvcrt.dll    
import printf msvcrt.dll
import scanf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    ; ...
    text db "give n=",0
    final db "n!=%d",0
    format db "%d",0
    a resd 1                  ; the variable will store the number n read from the console
    

; our code starts here
segment code use32 class=code
    factor:
        ;to implement the problem recursively we need to break it in cases
        ;to compute the factorial we have two cases:
        ;n!=n*(n-1)!       - current iteration
        ;0!=1                  - stop condition
        ;the subprogram will repeat itsealf until ecx=0 when we make eax = 1 and return to the previous step
        mov ecx, [esp+4] ;move in ecx the number of steps that need to be done
        jecxz sf ;if ecx is 0 we jump to the label sf to start computing the factorial
        ;if we pass the comparison with 0 the we are at the first case of recursivity 
        ;the formula is n!=n*(n-1)!
        dec ecx; decrease ecx to call again the function for the next step
        push ecx;  push on the stack the current value of n 
        call factor; call the function with the current parameter with the value from the stack
        mul dword [esp+8]; multiply by the value of the current step
        add esp,4; free the stack to go back to the previous step
        jmp return; jump to the label return to step out from the subprogram
        
   sf:
        mov eax,1;because our recursivity has two cases we reached the case when ecx is 0 and return 1 – the stop condition 
        ;0!=1
        return:
        ret ;we go back to the previous step or to the main program
   start:
        ; ...
        ;writting the message
        push dword text
        call [printf]
        add esp,4

        ;read n from the console
        push dword a
        push dword format
        call [scanf]
        add esp,4*2 
        
        mov ecx,0
        mov eax,0;prepare the registers for the call
        push dword [a] ;save on the stack n
        call factor ;call the function

        ;writting the result
        push eax
        push final
        call [printf]
        ; exit(0)
        push dword 0; push the parameter for exit onto the stack
        call [exit]; call exit to terminate the program