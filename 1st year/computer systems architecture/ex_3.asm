bits 32 ;asamblare și compilare pentru arhitectura de 32 biți
; definim punctul de intrare in programul principal
global start

; declaram functiile externe necesare programului nostru 
extern exit ; indicam asamblorului ca exit exista, chiar daca noi nu o vom defini
import exit msvcrt.dll  ; exit este o functie care incheie procesul, este definita in msvcrt.dll
        ; msvcrt.dll contine exit, printf si toate celelalte functii C-runtime importante

; segmentul de date in care se vor defini variabilele 
segment data use32 class=data

a dw 0111_0111_0101_0111b
b dw 1001_1011_1011_1110b
c dd 0


; segmentul de cod
segment code use32 class=code
start:

;Given the word A and the byte B, compute the doubleword C:
;the bits 0-3 of C have the value 1
;the bits 4-7 of C are the same as the bits 0-3 of A
;the bits 8-13 of C have the value 0
;the bits 14-23 of C are the same as the bits 4-13 of A
;the bits 24-29 of C are the same as the bits 2-7 of B
;the bits 30-31 have the value 1

mov EBX, 0; we'll store the result here
mov BX, 0000_0000_0000_1111b ; the bits 0-3 have the value 1
mov EAX, 0;
mov AX, [a]; AX = 0111_0111_0101_"0111"b
mov CL, 4;
rol AX, CL; AX = 0111_0101_"0111"_0111b, CF = 1
and AX, 0000_0000_1111_0000b; AX = 0000_0000_0111_0000
or EBX, EAX; EBX = 0000_0000_0000_0000_0000_0000_0111_1111b
mov AX, [a]; AX = 01"11_0111_0101"_0111b (could've done it directly)
and AX, 0011_1111_1111_0000b; AX = 00"11_0111_0101"_0000b isolated a's 4-13 bits
mov CL, 10; 
rol EAX, CL; EAX = 0000_0000_.1101_1101_01.00_0000_0000_0000b
or EBX, EAX; EBX = 0000_0000_1101_1101_0100_0000_0111_1111b
mov EAX, 0;
mov AX, [b]; AX = 1001_1011_1011_1110b
and AX, 0000_0000_1111_1100b; AX = 0000_0000_1011_1100b isolated b's 2-7 bits
mov CL, 22;
rol EAX, CL; EAX = 0010_1111_0000_0000_0000_0000_0000_0000b
or EBX, EAX; EBX = 0010_1111_1101_1101_0100_0000_0111_1111b
or EBX, 1100_0000_0000_0000_0000_0000_0000_0000b; EBX = 1110_1111_1101_1101_0100_0000_0111_1111b

; ... 

    ; exit(0)
    push dword 0 ; se pune pe stiva parametrul functiei exit
    call [exit] ; apelul functiei exit pentru terminarea executiei programului
