# RobotSystem2021_DeviceDriver
- RaspberryPi4を使用して, 入力した計算式の計算結果を, LEDを制御し, 2進数で表示するデバイスドライバを作成しました. 4096未満の有理数を表示でき, 整数部分は3Byte, 小数部分は1Byteで表します. 
---
## 動作環境
- Ubuntu 20.04.3 LTS
- RaspberryPi4
---
## 使用するもの
- RaspberryPi4
- USBケーブル TypeC
- ブレッドボード
- LED, 抵抗(200Ω), ジャンパ線(オス-メス): 各17個
---
## 配線図
- 配線を行う際は,以下の実際の写真と回路図, 各LEDとGPIOピンの対応表を参考にしながら行ってください. 
### 実際に配線した写真
![figure](https://user-images.githubusercontent.com/91446273/145028123-3f1e35ad-0464-444b-ad85-98b0b1590e61.png)
- 黄, オレンジ, 赤色のLEDが整数部分を表し 順番に1, 2, 3Byte目を表します. 
- 緑色のLEDは整数と小数の区切りのピリオドを表しています. 
- 青色のLEDは小数部分を表します. 
### 回路図
![image](https://user-images.githubusercontent.com/91446273/145198164-654ad622-f4de-467d-a934-a727d276d2cb.png)
### 各LEDとGPIOピンの対応表
- RaspberryPi4のピン配置は[こちら](https://www.raspberrypi.com/documentation/computers/os.html#gpio-and-the-40-pin-header)を参考にしてください. 

| LED | GPIO番号 |
| :-------|:------|
| LED0 | 21 |
| LED1 | 20 |
| LED2 | 26 |
| LED3 | 16 |
| LED4 | 19 |
| LED5 | 13 |
| LED6 | 12 |
| LED7 | 6 |
| LED8 | 5 |
| LED9 | 25 |
| LED10 | 24 |
| LED11 | 23 |
| LED12 | 22 |
| LED13 | 27 |
| LED14 | 18 |
| LED15 | 17 |
| LED16 | 4 |
---
## 実行方法
### セットアップ
```sh
git clone https://github.com/makotoyoshigoe/RobotSystem2021_DeviceDriver.git
cd RobotSystem2021_DeviceDriver
./setup.bash
```
### pythonスクリプトを実行
```sh
python3 calc.py
#input formula:
```
### 計算式を入力
#### 四則演算
```sh
input formula:29+3
```
```sh
input formula:29-3
```
```sh
input formula:4*12
```
```sh
input formula:12/3
```
```sh
input formula:ans+4 #ansを入力すると, 前回の計算結果を引き継いで使える. 
```
#### 小数・負の数の計算
```sh
input formula:3.6+7.8
```
```sh
input formula:5.7-10.4
```
#### エラー処理
```sh
input formula:2500+2100
#計算結果が4096以上なので, エラー処理(LEDの点滅)を行う.
```
```sh
input formula:15/0
#this formula cannot be calculated.
```
#### 隠し(?)機能
```sh
input formula:w
#LEDが順番に点灯する. waveの「w」.
```
#### 終了
```sh
input formula:q
```
### デバイスファイルの削除
```sh
sudo rmmod calculator
make clean
```
---
## 実際に動かしている様子
YouTubeリンク: https://youtu.be/hRQb1wQBKWY 
