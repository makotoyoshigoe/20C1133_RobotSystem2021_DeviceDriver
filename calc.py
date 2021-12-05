#!/usr/bin/env python3

def main():
    fomula = ''
    while True:
        fomula = input('input formula:')
        if fomula == 'q':
            break
        ans = eval(fomula)
        print(f'ans={ans}')

if __name__ == '__main__':
    main()
