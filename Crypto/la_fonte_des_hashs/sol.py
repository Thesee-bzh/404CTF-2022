#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

# from https://asecuritysite.com/subjects/chapter88
sbox_inv = ['01010010', '00001001', '01101010', '11010101', '00110000', '00110110', '10100101', '00111000', '10111111', '01000000', '10100011', '10011110', '10000001', '11110011', '11010111', '11111011', '01111100', '11100011', '00111001', '10000010', '10011011', '00101111', '11111111', '10000111', '00110100', '10001110', '01000011', '01000100', '11000100', '11011110', '11101001', '11001011', '01010100', '01111011', '10010100', '00110010', '10100110', '11000010', '00100011', '00111101', '11101110', '01001100', '10010101', '00001011', '01000010', '11111010', '11000011', '01001110', '00001000', '00101110', '10100001', '01100110', '00101000', '11011001', '00100100', '10110010', '01110110', '01011011', '10100010', '01001001', '01101101', '10001011', '11010001', '00100101', '01110010', '11111000', '11110110', '01100100', '10000110', '01101000', '10011000', '00010110', '11010100', '10100100', '01011100', '11001100', '01011101', '01100101', '10110110', '10010010', '01101100', '01110000', '01001000', '01010000', '11111101', '11101101', '10111001', '11011010', '01011110', '00010101', '01000110', '01010111', '10100111', '10001101', '10011101', '10000100', '10010000', '11011000', '10101011', '00000000', '10001100', '10111100', '11010011', '00001010', '11110111', '11100100', '01011000', '00000101', '10111000', '10110011', '01000101', '00000110', '11010000', '00101100', '00011110', '10001111', '11001010', '00111111', '00001111', '00000010', '11000001', '10101111', '10111101', '00000011', '00000001', '00010011', '10001010', '01101011', '00111010', '10010001', '00010001', '01000001', '01001111', '01100111', '11011100', '11101010', '10010111', '11110010', '11001111', '11001110', '11110000', '10110100', '11100110', '01110011', '10010110', '10101100', '01110100', '00100010', '11100111', '10101101', '00110101', '10000101', '11100010', '11111001', '00110111', '11101000', '00011100', '01110101', '11011111', '01101110', '01000111', '11110001', '00011010', '01110001', '00011101', '00101001', '11000101', '10001001', '01101111', '10110111', '01100010', '00001110', '10101010', '00011000', '10111110', '00011011', '11111100', '01010110', '00111110', '01001011', '11000110', '11010010', '01111001', '00100000', '10011010', '11011011', '11000000', '11111110', '01111000', '11001101', '01011010', '11110100', '00011111', '11011101', '10101000', '00110011', '10001000', '00000111', '11000111', '00110001', '10110001', '00010010', '00010000', '01011001', '00100111', '10000000', '11101100', '01011111', '01100000', '01010001', '01111111', '10101001', '00011001', '10110101', '01001010', '00001101', '00101101', '11100101', '01111010', '10011111', '10010011', '11001001', '10011100', '11101111', '10100000', '11100000', '00111011', '01001101', '10101110', '00101010', '11110101', '10110000', '11001000', '11101011', '10111011', '00111100', '10000011', '01010011', '10011001', '01100001', '00010111', '00101011', '00000100', '01111110', '10111010', '01110111', '11010110', '00100110', '11100001', '01101001', '00010100', '01100011', '01010101', '00100001', '00001100', '01111101']

def xor(a,b):
    res = ""
    for i in range(len(a)):
            res += str(int(a[i]) ^ int(b[i]))
    return res

def sbox_ope_inv(binary):
    for i in range(len(binary)):
        index = int(binary[i], 2)
        binary[i] = sbox_inv[index]

def phase2_inv(binary):
    for i in reversed(range(1,len(binary))):
        for j in reversed(range(i)):
            binary[i] = xor(binary[i], binary[j])

def hex2bits(hex_str):
    binary = []
    for c in bytes(bytearray.fromhex(hex_str)):
        binary.append(format(c, '08b'))
    return binary

def h_inv(hash_str):
    binary = hex2bits(hash_str)
    sbox_ope_inv(binary)
    phase2_inv(binary)
    phase2_inv(binary)
    phase2_inv(binary)
    print(''.join([chr(int(x, 2)) for x in binary]))

hash_str = '18f2048f7d4de5caabd2d0a3d23f4015af8033d46736a2e2d747b777a4d4d205'
h_inv(hash_str)

