# Crypto / Weak signature

## Challenge
Un nouveau système a été mis en place pour exécuter du code de façon sécurisée sur l'infrastructure. Il suffit d'envoyer une archive signée et encodée en base 64 pour exécuter le code Python qu'elle contient !

Vous trouverez la documentation de ce système et un exemple en pièces jointes. Tentez de voir si vous ne pourriez pas l'exploiter afin de lire le précieux fichier `flag.txt`.

## Inputs
- Server: `challenge.404ctf.fr:32441`
- [ARCHIVE.md](./ARCHIVE.md)
- [script.py.zsig](./script.py.zsig)
- [sign.py](./sign.py)

## Solution
So we're given some python code to sign and verify a signature, a signed example and also the format of a signed file. The example contains this simple python payload `print("Hello, CTF player!")` that is executed on the server when the signature is verified.

To be more precise, the full payload is longer and includes a comment line:
```python
# This is a demo script. It doesn\'t do much, but I like it. You can use it too if you want :D
print("Hello, CTF player!")
```

The verification algorithm is as follow (from [ARCHIVE.md](./ARCHIVE.md)):
```
- Compute the checksum of the data section
- Decrypt the signature using the public key
- Compare the computed checksum with the decrypted signature
```

So we already have a valid signature from the signed example [script.py.zsig](./script.py.zsig). And so that valid signature matches the checksum of the example payload. If we could craft our payload (to read file `flag.txt`) so that its checksum exactly matches the checksum of the example payload, we could simply replace our payload in the signed example, send it to the server, and it should pass the signature verification !

Here is the function that computes the checksum of the data:
```python
def checksum(data: bytes) -> int:
    # Sum the integer value of each byte and multiply the result by the length
    chksum = sum(data) * len(data)

    return chksum
```

Providing we craft a payload of `same length`, it must be possible to achieve `same sum()`. The example payload is 122 bytes (including the newlines) and to read file `flag.txt`, we would like to execute payload `print(open("flag.txt","r").read())\n`, which is 35 bytes. So it should be possible to fill our payload with a comment line carefully chosen such that the `sum()` of our payload matches the one of the example payload.

So our goal is to use the signed example [script.py.zsig](./script.py.zsig) as follow:
- Retrieve the signature, the data size and the data itself ([ARCHIVE.md](./ARCHIVE.md) gives us the format)
- Compute the data length and data checksum
- Build new data with exact same length but different payload (to read flag.txt), including a comment line (to match the length)
- Adjust the comment line in the payload to exactly match the checksum of the example payload

Retrieve the signature, the data size and the data itself; Also compute the data checksum:
```python
status = verify('script.py.zsig', mod)
signature, size, data = status[0], status[1], status[2]
chksum = checksum(data)
```

Build new data with different payload (to read flag.txt). Add a comment line `#UUUUU...`, up to the data length, so that both sizes are equal.  This comes out try/error iterations to target `sum(data)` as closely as possible:
```python
payload = b'print(open("flag.txt","r").read())\n'
chksum_payload = checksum(payload)

payload += b'#'
n = (size - len(payload))
payload += n * b'U'
chksum_payload = checksum(payload)
```

Finally adjust payload's last char to exactly match sum(data):
```python
offset = sum(data) - sum(payload)
try:
    c = chr(ord('U') + offset)
except:
    print("Can't adjust last char...")
    sys.exit()
payload = payload[:-1]
payload += c.encode()
chksum_payload = checksum(payload)
assert(chksum == chksum_payload)
```

Here is our final payload; It has `same length` and `same sum` as the example payload, so `same checksum`:
```python
print(open("flag.txt","r").read())
#UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUA
```

Now that the checksum matches, we can build out signed file using the signature from the signed example and our payload:
```python
signature_bytes = signature.to_bytes(300, "big")
size_bytes = len(data).to_bytes(4, "big")
out_bytes = b"\x01ZSig\x02" + signature_bytes + b"\x03" + size_bytes + b"\x04" + payload
with open('flag.zsig', "wb+") as f:
    f.write(out_bytes)
```

Let's run our code to generate our signed file, `base64` encode it and send it to the server:
```console
$ python3 sol.py
$ base64 flag.zsig -w 0 > flag.zsig.b64
$ nc challenge.404ctf.fr 32441 < flag.zsig.b64
Send me a signed archive encoded in base 64:
404CTF{Th1s_Ch3cksum_W4s_Tr4sh}
```

## Python code
Complete solution in [sol.py](./sol.py)

## Flag
404CTF{Th1s_Ch3cksum_W4s_Tr4sh}
