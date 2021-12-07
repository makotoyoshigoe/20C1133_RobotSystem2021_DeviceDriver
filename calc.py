#!/usr/bin/env python3
POSITIVE_BIT = 12
NEGATIVE_BIT = 4
PERIOD = 2
ERR = 4096
#正数を2進数に変換する関数
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
#10進数を2進数に変換する関数
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
#ビット反転を行う関数
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
#メイン処理
def main():
    formula = ''
    path = '/dev/calculator0'#デバイスファイルのパス
    #qが入力されるまで繰り返す
    while formula != 'q':
        formula = input('input formula:')#入力
        try:
            if formula == 'w':
                binary = 'w'
            else:
                ans = eval(formula)
                if ans >= ERR:#エラー処理(計算結果が4096のとき)
                    binary = 'e'
                else:#通常の処理
                    binary = complement(convert_binary(abs(ans))) if ans < 0 else convert_binary(ans)
                    print(f'ans={ans}, {binary}')
            with open(path, mode='w') as f:#デバイスファイルに書き込み
                for i in range(len(binary)):
                    f.write(str(binary[i]))
        except:
            print('this formula cannot be calculated.')

if __name__ == '__main__':
    try:
        main()
    except:
        print('error')
