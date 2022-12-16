#!/usr/bin/env python3
import shutil
import random
import argparse

x64_no_instruction_sets = [
    [
        'nop'
    ],
    [
        'xchg eax, eax'
    ]
]

x86_no_instruction_sets = [
    [
        'nop'
    ],
    [
        'xchg eax, eax'
    ]
]


def tab(x):
    result = []
    for y in x:
        result.append(f"    {y}")
    return result


x64_no_instruction_sets = list(map(tab, x64_no_instruction_sets))
x86_no_instruction_sets = list(map(tab, x86_no_instruction_sets))

assembly_instructions = [
    'push',
    'pop',
    'ret',
    'mov',
    'xchg',
    'xor',
    'call',
    'loop',
    'test',
    'jmp',
    'jz',
    'jnz',
    'add',
    'dec',
    'shl',
    'shr',
    'cmp',
    'loopnz',
]


def starts_with_pneumonic(line):
    for i in assembly_instructions:
        if line.strip().lower().startswith(f"{i} "):
            return True
    return False


def morph(shellcode_file, morph_percentage, verbose, x86_mode):
    '''
    Assumes max one empty line between each function
    '''
    with open(shellcode_file, 'r') as f:
        shellcode_source = f.read().split('\n')

    num_of_lines = len(shellcode_source)
    print(f"Initial length: {num_of_lines}")

    x = 0
    started = False
    while x < (num_of_lines - 2):
        x += 1

        if verbose:
            print(f"Processing:\n{shellcode_source[x]}")

        if shellcode_source[x].strip().startswith(";") or not starts_with_pneumonic(shellcode_source[x]):
            if verbose:
                print("Not instruction line")
            continue

        if verbose:
            print(f"Rolling the dice...")
        if random.random() > (1 - (morph_percentage / 100)):
            if verbose:
                print(f"Score! Picking instructions")
            if x86_mode:
                instructions = random.choice(x86_no_instruction_sets)
            else:
                instructions = random.choice(x64_no_instruction_sets)

            for instruction in instructions:
                if verbose:
                    print(f"Inserting instruction at offset {x}")
                    print(f"{instruction}")
                shellcode_source.insert(x, instruction)
                x += 1
                num_of_lines += 1
        elif verbose:
            print(f"Not this time...")

    with open(shellcode_file, 'w') as f:
        print(f"Final length: {len(shellcode_source)} lines")
        f.write('\n'.join(shellcode_source))


def create_arg_parser():
    parser = argparse.ArgumentParser(description='Insert random no-instructions at random locations into assembly shellcode')
    parser.add_argument("-t", "--shellcode-template", help="the template shellcode file to use", default='Source/ASM/shellcode-template.asm')
    parser.add_argument("-s", "--shellcode-file", help="where to write the morphed file to", default='Source/ASM/shellcode.asm')
    parser.add_argument("-m", "--morph-percentage", help="percentage increase of the number of instructions with no-instructions", type=int, default=15)
    parser.add_argument("-v", "--verbose", help="enable verbose mode", action="store_true")
    parser.add_argument("-x86", "--x86", help="x86 mode", action="store_true")
    return parser


def main():

    print("##################")
    print("It's Morphin' Time")
    print("##################")

    parser = create_arg_parser()
    args = parser.parse_args()

    shellcode_file = args.shellcode_file
    shellcode_template = args.shellcode_template

    print("Copying template...")
    shutil.copyfile(shellcode_template, shellcode_file)
    print("Morphing shellcode...")
    if args.x86:
        print("x86 mode")
    morph(shellcode_file, args.morph_percentage, args.verbose, args.x86)
    print("Done")


if __name__ == '__main__':
    main()
