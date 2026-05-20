section .data
    msg db "Press a key: ",10
    len equ $-msg

    output db "You Pressed: "
    outlen equ $-output

section .bss
    char resb 1

section .text
    global _start

_start:

    ; Print "Press a key"
    mov eax,4
    mov ebx,1
    mov ecx,msg
    mov edx,len
    int 0x80

    ; Read keyboard input
    mov eax,3
    mov ebx,0
    mov ecx,char
    mov edx,1
    int 0x80

    ; Print output message
    mov eax,4
    mov ebx,1
    mov ecx,output
    mov edx,outlen
    int 0x80

    ; Print entered character
    mov eax,4
    mov ebx,1
    mov ecx,char
    mov edx,1
    int 0x80

    ; Exit program
    mov eax,1
    xor ebx,ebx
    int 0x80