; =========================================================
; RT64 LINUX CORE (stable syscall layer)
; =========================================================

SYS_read  equ 0
SYS_write equ 1
SYS_exit  equ 60

STDIN  equ 0
STDOUT equ 1


; -------------------------
; write(fd=rdi, buf=rsi, len=rdx)
; -------------------------
rt_write:
    mov rax, SYS_write
    syscall
    ret


; -------------------------
; read(fd=rdi, buf=rsi, len=rdx)
; -------------------------
rt_read:
    mov rax, SYS_read
    syscall
    ret


; -------------------------
; exit(code=rdi)
; -------------------------
rt_exit:
    mov rax, SYS_exit
    syscall
    ret
