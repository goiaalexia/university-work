bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, scanf, fopen, fread, fprintf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll
import fopen msvcrt.dll         
import fread msvcrt.dll
import fprintf msvcrt.dll  
import printf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    format_1 db "%d", 0
    format_2 db "%s", 0
    access_mode_append db "a", 0
    access_mode_reading db "r+", 0
    file_name_afisare resb 1
    file_name_citire resb 1
    file_descriptor_afisare dd -1, 0
    file_descriptor_citire dd -1, 0
    len equ 1;
    text db 0, 0;
    chestie dd 0,0;
    
    
; our code starts here
segment code use32 class=code
start:    
    
    push dword file_name_citire    ; CITIM NUMELE FISIERULUI DE INTRARE  (IN)
    push dword format_2
    call [scanf]
    add esp, 4*2
    
    push dword access_mode_reading   ; CREAM FISIERUL DE CITIRE IN MOD READING
    push dword file_name_citire
    call [fopen]
    add esp, 4*2
    
    mov [file_descriptor_citire], eax  ; VERIFICAM DACA S-A CREAT
    cmp eax, 0
    je final
    
    
    push dword file_name_afisare    ; CITIM NUMELE FISIERULUI DE IESIRE (IN2)
    push dword format_2
    call [scanf]
    add esp, 4*2
    
    push dword access_mode_append   ; CREAM FISIERUL DE CITIRE IN MOD APPEND
    push dword file_name_afisare
    call [fopen]
    add esp, 4*2
    
    mov [file_descriptor_afisare], eax  ; VERIFICAM DACA S-A CREAT
    cmp eax, 0
    je final
    
    ; CITIM DIN FISIER SIRUL SI APOI IL PARCURGEM, VERIFICAND DACA AM INTALNIT UN CARACTER CARE SA FIE INTRE 0 SI 9
    
    loopity:        ; CITIM CARACTER CU CARACTER, PANA CAND DAM DE .
    
        push dword [file_descriptor_citire]  ; CITIM SIRUL DIN FISIER
        push dword len
        push dword 1
        push dword text
        call [fread]
        add esp, 4*4
        
        mov al, [text]
        
        cmp al, '.'                    ; DACA E PUNCT SARIM, CA INSEAMNA CA AM AJUNS LA FINAL.
        je afisare_punct_apoi_final
        cmp al, '0'                  ; DACA E MAI MARE SAU EGAL CU 0, CONTINUAM VERIFICARILE
        jae potentiala_cifra
        jmp afisare_standard              ; ALTFEL AFISAM
        
        potentiala_cifra:
        cmp al, '9'               ; DACA E MAI MIC DECAT 9 INSEAMNA CA E BUN.
        jb am_gasit_cifra
        je e_9
        jmp afisare_standard             ; ALTFEL AFISAM 
        
        am_gasit_cifra:
        add al, 1              ; ADAUGAM 1 CIFREI
        jmp afisare_standard
        
        
        e_9:
        mov al, '0'
        jmp afisare_standard
        
        afisare_standard:
        mov [chestie], al
        push dword chestie                        ; AFISAM CHESTIA 
        push dword [file_descriptor_afisare]
        call [fprintf]
        add esp, 4*2
        loop loopity                          ; CONTINUAM LOOP-UL DACA NU AM AJUNS LA FINAL
        
                
        afisare_punct_apoi_final:
        push dword text                      ; AFISAM ULTIMUL PUNCT SI APOI IESIM
        push dword [file_descriptor_afisare]
        call [fprintf]
        add esp, 4*2
        jmp final
        
        
    final:
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program
