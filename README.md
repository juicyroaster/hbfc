
# hbfc (Hasty BrainFuck Compiler)

hbfc is a compiler for BrainFuck written in python that compiles to x86_64 linux FASM. It includes its own runtime and stdlib that makes it independent from other libraries like libc.


## Installation

Clone the repo with:
```bash 
  git clone https://github.com/juicyroaster/hbfc.git 
```
Example test compilation:
```bash
  cd hbfc
  python3 src/main.py tests/hello_world.bf
```
    
## System Requirments

- FASM (SYSTEM WIDE ISNATLLATION, ADDED IN PATH)
- Python3 (PYTHON 3.7+, ADDED IN PATH)



## Contribution

Any pull requests and bug fixes will be welcomed.