#!/usr/bin/env python3

def convert_binary_int(dec):
    quo = dec
    mod = 0
    binary = []
    while True:
        quo, mod = divmod(quo, 2)
        binary.append(mod)
        if quo < 1:
            binary.append(quo)
            break
    print(len(binary))
    while len(binary) < 12:
        binary.append(0)
    binary.reverse()
    while len(binary) >= 13:
        binary.pop(0)
    return binary

def convert_binary(dec):
    p_int = int(dec)
    p_float = dec - p_int
    f_bin = []
    i_bin = convert_binary_int(p_int)
    i_bin.append(1)
    cnt = 0
    quo = p_float
    while cnt < 4:
        cnt += 1
        quo *= 2
        f_bin.append(int(quo))
        quo -= 1 if quo >= 1 else 0
    binary = i_bin + f_bin
    return binary

def main():
    fomula = ''
    while True:
        fomula = input('input formula:')
        if fomula == 'q':
            break
        ans = eval(fomula)
        binary = convert_binary(ans)
        print(f'ans={ans}, binary={binary}')

if __name__ == '__main__':
    main()
