#!/bin/bash -xve

make
sudo insmod calculator.ko
sudo chmod 666 /dev/calculator0
