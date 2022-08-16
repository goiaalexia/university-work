;S: '+', '4', '2', 'a', '@', '3', '$', '*'
;D: '@','$','*'
;Given a character string S, obtain the string D containing all special characters (!@#$%^&*) of the string S
bits 32 
global start        
extern exit ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll ; exit is a function that ends the calling process. It is defined in msvcrt.dll
; msvcrt.dll contains exit, printf and all the other important C-runtime specific functions
; our data is declared here (the variables needed by our program)
segment data use32 class=data
	s db '+', '4', '2', 'a', '@', '3', '$', '*' ; declare the string of bytes
	l equ $-s ; compute the length of the string in l
	d times l db 0 ; reserve l bytes for the destination string and initialize it
segment code use32 class=code
start:
	mov ecx, l ; we put the length l in ECX in order to make the loop
	mov esi, 0       
	Loopity:
		mov al, [s+esi]
        cmp al, '!'
        je good
        cmp al, '@'
        je good
        cmp al, '#'
        je good
        cmp al, '$'
        je good
        cmp al, '%'
        je good
        cmp al, '^'
        je good
        cmp al, '&'
        je good
        cmp al, '*'
        je good
        good:
		mov [d+esi], al    
		inc esi
	loop Loopity

	; exit(0)
	push dword 0 ; push the parameter for exit onto the stack
	call [exit] ; call exit to terminate the program