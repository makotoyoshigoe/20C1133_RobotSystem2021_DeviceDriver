#!/usr/bin/env python3
POSITIVE_BIT = 12
NEGATIVE_BIT = 4
PERIOD = 2
ERR = 4096

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
    while len(binary) < POSITIVE_BIT:
        binary.append(0)
    binary.reverse()
    while len(binary) >= POSITIVE_BIT+1:
        binary.pop(0)
    return binary

def convert_binary(dec):
    p_int = int(dec)
    p_float = dec - p_int
    f_bin = []
    i_bin = convert_binary_int(p_int)
    i_bin.append(PERIOD)
    quo = p_float
    for i in range(NEGATIVE_BIT):
        quo *= 2
        f_bin.append(int(quo))
        quo -= 1 if quo >= 1 else 0
    return i_bin + f_bin

def complement(arr):
    for i in range(len(arr)):
        if arr[i] == PERIOD:
            continue
        arr[i] = 1 if arr[i] == 0 else 0
    for i in range(-1, -len(arr), -1):
        if arr[i] == 0:
            arr[i] = 1
            break
        elif arr[i] == 1:
            arr[i] = 0
    return arr

def main():
    formula = ''
    path = '/dev/calculator0'
    while formula != 'q':
        formula = input('input formula:')
        try:
            if formula == 'w':
                binary = 'w'
            else:
                ans = eval(formula)
                if ans >= ERR:
                    binary = 'e'
                else:
                    binary = complement(convert_binary(abs(ans))) if ans < 0 else convert_binary(ans)
                    print(f'ans={ans}, {binary}')
            with open(path, mode='w') as f:
                for i in range(len(binary)):
                    f.write(str(binary[i]))
        except:
            print('this formula cannot be calculated.')

if __name__ == '__main__':
    try:
        main()
    except:
        print('error')
