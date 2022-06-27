#!/usr/bin/python3

from pwn import *

# Connect to target, skip header
target = remote('challenge.404ctf.fr', 32128)

def get_n_e_secret():
    # Voici le message...
    # < Ciphered Flag>
    skip = target.recvline()
    line = target.recvline().decode('utf-8')
    secret = int(line)
    # J'en profite aussi...
    skip = target.recvline()
    # N = ...
    line = target.recvline()[3::].decode('utf-8')
    n = int(line)
    # e = ...
    line = target.recvline()[3::].decode('utf-8')
    e = int(line)
    #
    # Ceci étant dit...
    #
    skip = target.recvline()
    skip = target.recvline()
    skip = target.recvline()
    # Return n, e, secret
    return n, e, secret

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
    n, e, secret = get_n_e_secret()
    c2 = pow(2, e)
    P = send_recv(secret*c2)
    F = P//2
    hex_ = hex(F)[2::]
    return bytes.fromhex(hex_).decode()

flag = get_flag()
print(flag)

# 404CTF{L3s_0r4cl3s_RSA_s0n7_si_fr4g1l35}
