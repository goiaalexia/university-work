bits 32 ;asamblare și compilare pentru arhitectura de 32 biți
; definim punctul de intrare in programul principal
global start

; declaram functiile externe necesare programului nostru 
extern exit ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import exit msvcrt.dll  ; exit este o functie care incheie procesul, este definita in msvcrt.dll
        ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante

; segmentul de date in care se vor defini variabilele 
segment data use32 class=data
a db 100;
b dw 1000;
c dd 5000;
d dq 10000;

; segmentul de cod
segment code use32 class=code
start: ; a - byte, b - word, c - double word, d - qword - Unsigned
;(b+b)+(c-a)+d
mov EAX, 0;
mov DX, 0;
mov AX, [b]; AX = b
add AX, [b]; AX = b+b
adc DX, 0;
push DX;
push AX;
pop EAX; EAX = b+b
mov EBX, [c]; EBX = c
sub BL, [a]; EBX = c-a
sbb BH, 0;
add EAX, EBX; EAX = b+b+c-a
mov EDX, 0;
add EAX, dword[d];
adc EDX, dword[d+4]; less registries better life


; ... 

    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
