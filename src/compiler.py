import os


def src_root():
    return os.path.dirname(os.path.abspath(__file__))


def resolve(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing file: {path}")
    return os.path.abspath(path)


def compile_bf64_linux(src: str) -> str:
    SRC = src_root()

    stdio_path = resolve(os.path.join(SRC, "stdlib", "stdio_linux.asm"))

    out = [
        "format ELF64 executable",
        "entry start",
        "",
        f'include "{stdio_path}"',
        "",
        "segment readable writable",
        "tape rb 30000",
        "",
        "segment readable executable",
        "start:",
        "    mov r12, tape",
        ""
    ]

    i = 0
    loop_stack = []
    loop_id = 0

    while i < len(src):
        c = src[i]

        # pointer ops
        if c in "><":
            val = 0
            while i < len(src) and src[i] in "><":
                val += 1 if src[i] == ">" else -1
                i += 1
            if val > 0:
                out.append(f"    add r12, {val}")
            elif val < 0:
                out.append(f"    sub r12, {-val}")
            continue

        # value ops
        if c in "+-":
            val = 0
            while i < len(src) and src[i] in "+-":
                val += 1 if src[i] == "+" else -1
                i += 1
            if val > 0:
                out.append(f"    add byte [r12], {val}")
            elif val < 0:
                out.append(f"    sub byte [r12], {-val}")
            continue

        # clear cell optimization
        if c == "[" and src[i:i+3] in ("[-]", "[+]"):
            out.append("    mov byte [r12], 0")
            i += 3
            continue

        # output
        if c == ".":
            out += [
                "    mov rsi, r12",
                "    call print_byte_ptr"
            ]

        # input
        elif c == ",":
            out += [
                "    call read_char",
                "    mov [r12], al"
            ]

        # loop start
        elif c == "[":
            lid = loop_id
            loop_id += 1
            loop_stack.append(lid)

            out.append(f"loop_start_{lid}:")
            out.append("    cmp byte [r12], 0")
            out.append(f"    je loop_end_{lid}")

        # loop end
        elif c == "]":
            if not loop_stack:
                raise Exception("Unmatched ]")

            lid = loop_stack.pop()

            out.append("    cmp byte [r12], 0")
            out.append(f"    jne loop_start_{lid}")
            out.append(f"loop_end_{lid}:")

        i += 1

    if loop_stack:
        raise Exception("Unmatched [")

    out += [
        "",
        "    xor rdi, rdi",
        "    call rt_exit"
    ]

    return "\n".join(out)
