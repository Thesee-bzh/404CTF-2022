#!/usr/bin/python3

from pwn import *

# Connect to target, skip header
target = remote('challenge.404ctf.fr', 30594)

def get_e_secret():
    # Il y a eu quelques petits...
    skip = target.recvline()
    # Je peux à nouveau...
    # < Ciphered Flag>
    skip = target.recvline()
    line = target.recvline().decode('utf-8')
    secret = int(line)
    # Par mesure de sécurité...
    skip = target.recvline()
    # e = ...
    line = target.recvline()[3::].decode('utf-8')
    e = int(line)
    #
    # Ceci étant dit...
    #
    skip = target.recvline()
    skip = target.recvline()
    skip = target.recvline()
    # Return e, secret
    return e, secret

def send_recv(c):
    req = str(c).encode()
    target.send(req + b'\n')
    # Voici ma réponse:
    # <resp>
    skip = target.recvline()
    line = target.recvline().decode('utf-8')
    resp = int(line)
    skip = target.recvline()
    return resp

def get_flag():
    e, secret = get_e_secret()
    c2 = pow(2, e)
    P = send_recv(secret*c2)
    F = P//2
    hex_ = hex(F)[2::]
    return bytes.fromhex(hex_).decode()

flag = get_flag()
print(flag)

# 404CTF{L3_m0dul3_357_t0uj0ur5_7r0uv4bl3}
