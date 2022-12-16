# Shellcode Mutator

Mutate nasm assembly source files using no-instruction sets (such as `nops`) to avoid signatures.

## Usage

```
##################
It's Morphin' Time
##################
usage: mutate.py [-h] [-t SHELLCODE_TEMPLATE] [-s SHELLCODE_FILE] [-m MORPH_PERCENTAGE] [-v] [-x86]

Insert random no-instructions at random locations into assembly shellcode

optional arguments:
  -h, --help            show this help message and exit
  -t SHELLCODE_TEMPLATE, --shellcode-template SHELLCODE_TEMPLATE
                        the template shellcode file to use
  -s SHELLCODE_FILE, --shellcode-file SHELLCODE_FILE
                        where to write the morphed file to
  -m MORPH_PERCENTAGE, --morph-percentage MORPH_PERCENTAGE
                        percentage increase of the number of instructions with no-instructions
  -v, --verbose         enable verbose mode
  -x86, --x86           x86 mode
```
