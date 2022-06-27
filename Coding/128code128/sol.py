#!/usr/bin/python3

from pwn import *
from PIL import Image
import numpy as np
from base64 import b64decode
import sys
import io

BLACK = (0, 0, 0)

# Code128 symbols
# Starts with: (espace, ascii=32, code128=212222)
OFFSET = 32
CODE = ('212222', '222122', '222221', '121223', '121322', '131222', '122213', '122312', '132212', '221213', '221312', '231212', '112232', '122132', '122231', '113222', '123122', '123221', '223211', '221132', '221231', '213212', '223112', '312131', '311222', '321122', '321221', '312212', '322112', '322211', '212123', '212321', '232121', '111323', '131123', '131321', '112313', '132113', '132311', '211313', '231113', '231311', '112133', '112331', '132131', '113123', '113321', '133121', '313121', '211331', '231131', '213113', '213311', '213131', '311123', '311321', '331121', '312113', '312311', '332111', '314111', '221411', '431111', '111224', '111422', '121124', '121421', '141122', '141221', '112214', '112412', '122114', '122411', '142112', '142211', '241211', '221114', '413111', '241112', '134111', '111242', '121142', '121241', '114212', '124112', '124211', '411212', '421112', '421211', '212141', '214121', '412121', '111143', '111341', '131141')

# Connect to target, skip header
target = remote('challenge.404ctf.fr', 30566)

def loop_code128():
    header = target.recvline()
    b64    = target.recvline()
    print(header.decode('utf-8'))
    print(b64)

    # Try to base64 decode
    try:
        data = b64decode(b64)
    except:
        return False

    # Open the image, get width, read 1st line of pixels
    # Translate 1st line in binary (1=Black, 0=White)
    #i = Image.open('file.png')
    i = Image.open(io.BytesIO(data))
    p = list(i.getdata())[0:i.size[0]]
    b = ''.join(['1' if x == BLACK else '0' for x in p])

    # Convert in code128 string
    code128 = ''
    cur = ''
    count = 0
    for new in b:
        if new != cur and count != 0:
            code128 += str(count)
            count = 1
        else:
            count += 1
        cur = new
    code128 += str(count)

    # Break code128 string into code128 characters
    # Revert to ASCII string
    l = [code128[x:x+6] for x in range(0, len(code128), 6)]
    s = ''.join([chr(CODE.index(x) + OFFSET) for x in l]).encode()
    print(s)

    # Send the decoded ASCII string
    target.send(s + b'\n')
    resp = target.recvline()
    print(resp.decode('utf-8'))

    # Did we succeed ?
    if b'Ouf' in resp:
        return True
    else:
        return False

result = True
while result == True:
    result = loop_code128()
