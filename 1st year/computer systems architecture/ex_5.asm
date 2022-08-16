;Problem. An array of words is given. Write an asm program in order to obtain an array of doublewords, where each doubleword will contain each nibble unpacked on a byte (each nibble will be preceded by a 0 digit), arranged in an ascending order within the doubleword.


bits 32 
global start
extern exit; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll; exit is a function that ends the calling process. It is defined in msvcrt.dll
; our data is declared here (the variables needed by our program)
segment data use32 class=data
	sir  dw  1432h, 7689h, 0BADCh
	len equ ($-sir)/2;the length of the string (in words)
    dest resd len*2
; our code starts here
segment code use32 class=code
    start:
    mov edi, dest
    mov ecx, len
	mov esi, sir
    loopity:
    mov eax, 0
    mov ebx, 0
    lodsw ; ax = 1234, al = 34
    mov bl, al ; bl = 34
    shr ax, 8 ; al = 12 
    mov dl, al ; dl = 12
    and al, 1111_0000b ; al = 10
    shl ax, 4 ; ax = 0100
    and dl, 0000_1111b ; dl = 02
    mov al, dl; ax = 0102
    mov dl, bl; dl = 34
    and bl, 1111_0000b ; bl = 30
    shl bx, 4; bx = 0300
    and dl, 0000_1111b ; dl = 04
    mov bl, dl; bx = 0304, ax:bx = 0102_0304
    cmp ah, al;
    jb is_good
    mov dl, al;
    mov al, ah;
    mov ah, dl;
    is_good:
    cmp bh, bl;
    jb is_good_again
    mov dl, bl;
    mov bl, bh;
    mov bh, dl;
    is_good_again: ; ax:bx = 0102_0304
    shl eax, 16;
    mov ax, bx;
    stosd;
    loop loopity
    
    
sfarsit:;end the program
           
        push dword 0; push the parameter for exit onto the stack
        call [exit]; call exit to terminate the program