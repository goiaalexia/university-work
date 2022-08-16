bits 32 ;asamblare și compilare pentru arhitectura de 32 biți
; definim punctul de intrare in programul principal
global start

; declaram functiile externe necesare programului nostru 
extern exit ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import exit msvcrt.dll  ; exit este o functie care incheie procesul, este definita in msvcrt.dll
        ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante

; segmentul de date in care se vor defini variabilele 
segment data use32 class=data
a db 100
b dd 1500
c db 200
x dq 100000
; segmentul de cod
segment code use32 class=code
start:
; x-(a*a+b)/(a+c/a); a,c-byte; b-doubleword; x-qword (UNSIGNED)
mov EAX, 0; vizual
mov AL, [a]; EAX = a
mul byte[a]; EAX = a*a
add EAX, [b]; EAX = a*a+b
mov EBX, EAX; EBX = a*a+b
mov EAX, 0;
add AL, [c]; AX = c 
mov CX, 0;
add CL, [a];
div CL; AL = c/a
add AL, [a];
adc AH, 0; AX = a+c/a
mov CX, AX; CX = a+c/a
mov EAX, EBX; EAX = a*a+b
div CX; AX = (a*a+b)/(a+c/a)
mov EBX, 0;
mov BX, AX; BX = (a*a+b)/(a+c/a)
mov EAX, dword[x];
mov EDX, dword[x+4]; higher part
sub EAX, EBX;
sbb EDX,0; EDX:EAX = x-(a*a+b)/(a+c/a)
; ... 

    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
