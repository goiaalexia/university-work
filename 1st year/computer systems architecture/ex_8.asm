; Se cere sa se citeasca de la tastatura un sir de numere, date in baza 10 ca numere cu semn (se citeste de la tastatura un sir de caractere si in memorie trebuie stocat un sir de numere).
bits 32 

global start        

; declare external functions needed by our program
extern exit, printf, scanf
import exit msvcrt.dll  
import fopen msvcrt.dll 
import printf msvcrt.dll 
import scanf msvcrt.dll
; %include  "sign.asm"


; our data is declared here (the variables needed by our program)
segment data use32 class=data
    sir resw 10
    message db "input: ", 0
    format  db "%s", 0  ; definim formatul
    format_print db "%d ", 0 ; format for writing
    n resw 1
                                    
segment code use32 class=code
    start:
        do_while:
            push dword message ; ! on the stack is placed the address of the string, not its value
            call [printf]      ; call function printf for printing
            add esp, 4*1       ; free parameters on the stack; 4 = size of dword; 1 = number of parameters
    
            push dword n       ; ! address of n, not value
            push dword format
            call [scanf]       ; call function scanf for reading
            add esp, 4 * 2     ; free parameters on the stack
            
            cmp word[n], 0 ; if the user inputs 0
            je final            
            positive:
            
            xor bx, bx; ebx = 00000000
            loopity:                
                cmp byte[n], 0; checking if we finished the number
                je out_the_loopity ; if yes, out we go     
                cmp byte[n], '-' ; checking if it's a negative number
                je negative                
                mov ax, 0;
                mov al, byte[n] ;
                sub al, 48 ; string -> number
                shr word[n], 8; next one
                cmp byte[n], 0; checking to see if there's more to add
                jne multiply
                
                multiply:
                    mul byte[10]
                    mov bl, al
                
                jmp loopity
            
            negative:
                neg bx
                jmp out_the_loopity
                
            out_the_loopity:
                ; add the number stored in BX to the string
                cld
                mov esi, sir
                mov ax, bx
                movsw
            jmp do_while
        

        
      final:
        
        ; exit(0)
        push    dword 0      
        call    [exit]       