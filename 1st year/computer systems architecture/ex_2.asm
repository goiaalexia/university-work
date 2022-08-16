;A file name is given (defined in the data segment). Create a file with the given name, then read numbers from the keyboard and write only the numbers divisible by 7 to file, until the value '0' is read from the keyboard.
bits 32 

global start        

; declare external functions needed by our program
extern exit, fopen, fprintf, fclose, printf, scanf
import exit msvcrt.dll  
import fopen msvcrt.dll 
import printf msvcrt.dll 
import fprintf msvcrt.dll
import fclose msvcrt.dll
import scanf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    n dw 0
    nume_fisier db "thing.txt", 0  ; numele fisierului care va fi creat
    mod_acces db "w", 0          ; modul de deschidere a fisierului -                                  ; w - pentru scriere. fisierul se va crea
    message db "n= ", 0
    format  db "%d", 0  ; definim formatul
    format_2 db "%d ", 0 ; format for writing
    descriptor_fis dd -1         ; variabila in care vom salva descriptorul fisierului - necesar pentru a putea face referire la fisier
                                    
segment code use32 class=code
    start:
        ; apelam fopen pentru a crea fisierul
        ; functia va returna in EAX descriptorul fisierului sau 0 in caz de eroare
        ; eax = fopen(nume_fisier, mod_acces)
        push dword mod_acces     
        push dword nume_fisier
        call [fopen]
        add esp, 4*2                ; eliberam parametrii de pe stiva

        mov [descriptor_fis], eax   ; salvam valoarea returnata de fopen in variabila descriptor_fis
        
        ; verificam daca functia fopen a creat cu succes fisierul (daca EAX != 0)
        cmp eax, 0
        je final
        
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
            
            mov AX, [n]
            mov BL, 7
            div BL
            cmp AH, 0 ; if the number is divisible we add it
            je trueee
            jmp do_while
            
            trueee:
                push dword [n]
                push dword format_2
                push dword [descriptor_fis]
                call [fprintf]
                add esp, 4*3
                jmp do_while
        
        ; apelam functia fclose pentru a inchide fisierul
        ; fclose(descriptor_fis)
        push dword [descriptor_fis]
        call [fclose]
        add esp, 4
        
      final:
        
        ; exit(0)
        push    dword 0      
        call    [exit]       