#!/usr/bin/python3

s = '4/2@PAu<+ViNgg%^5NS`#J\u001fNK<XNW(_'
p = ''.join([chr(ord(s[i]) + i) for i in range(len(s))])
print(p)

# 404CTF{C3_sYst3mE_es7_5ecUrisE}
