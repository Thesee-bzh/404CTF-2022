#!/usr/bin/python3

data = ''
with open("ip_len.txt", "r") as f:
    for line in f:
        length = int(line.strip())
        if length:
            data += chr(length - 28)

print(data)

# 404CTF{Un_p1ng_p0ng_p4s_si_1nn0c3nt}
