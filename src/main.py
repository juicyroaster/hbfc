import sys
import subprocess
import os
from compiler import compile_bf64_linux


def build(asm_code: str, out_name: str):
    asm_file = out_name + ".asm"

    with open(asm_file, "w") as f:
        f.write(asm_code)

    print(f"[+] Wrote {asm_file}")

    subprocess.run(["fasm", asm_file, out_name], check=True)
    os.chmod(out_name, 0o755)

    print(f"[+] Built {out_name}")
    return out_name


def main():
    if len(sys.argv) < 2:
        print("usage: python3 main.py file.bf [-o out] [--run]")
        sys.exit(1)

    input_file = sys.argv[1]
    output = "a.out"
    run = False

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "-o":
            output = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--run":
            run = True
            i += 1
        else:
            i += 1

    with open(input_file) as f:
        src = f.read()

    asm = compile_bf64_linux(src)
    binary = build(asm, output)

    if run:
        print("[+] Running...")
        subprocess.run(["./" + binary])


if __name__ == "__main__":
    main()
