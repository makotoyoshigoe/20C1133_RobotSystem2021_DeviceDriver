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
    #print(len(binary))
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
    i_bin.append(2)
    cnt = 0
    quo = p_float
    for i in range(4):
        quo *= 2
        f_bin.append(int(quo))
        quo -= 1 if quo >= 1 else 0
    binary = i_bin + f_bin
    return binary

def inverse_bit(arr):
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[i] = 1
        elif arr[i] == 1:
            arr[i] = 0
    for i in range(-1, -len(arr), -1):
        if arr[i] == 0:
            arr[i] = 1
            break
        elif arr[i] == 1:
            arr[i] = 0
    return arr

def main():
    formula = ''
    path = 'log.txt'
    while formula != 'q':
        formula = input('input formula:')
        try:
            ans = eval(formula)
            binary = inverse_bit(convert_binary(abs(ans))) if ans < 0 else convert_binary(ans)
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
