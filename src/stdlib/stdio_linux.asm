include "../rt/rt64_linux.asm"

; rsi = buffer pointer

print_byte_ptr:
    mov rdi, STDOUT
    mov rdx, 1
    call rt_write
    ret


print_char:
    sub rsp, 8
    mov [rsp], dil

    mov rdi, STDOUT
    mov rsi, rsp
    mov rdx, 1
    call rt_write

    add rsp, 8
    ret


read_char:
    sub rsp, 8

    mov rdi, STDIN
    mov rsi, rsp
    mov rdx, 1
    call rt_read

    mov al, [rsp]
    add rsp, 8
    ret
