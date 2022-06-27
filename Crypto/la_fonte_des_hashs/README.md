# Crypto / La fonte des hashs

## Challenge :star:
Nos experts ont réussi à intercepter un message de Hallebarde : `18f2048f7d4de5caabd2d0a3d23f4015af8033d46736a2e2d747b777a4d4d205`

Malheureusement il est haché ! L'équipe de rétro-ingénierie vous a laissé cette note :

> Voici l'algorithme de hachage. Impossible de remonter le haché mais vous, vous trouverez peut être autre chose. Voici comment lancer le hachage : python3 hash.py [clair]
> PS : Les conversations interceptées parlaient d'algorithme "très frileux" ...

## Inputs
- Python script: [hash.py](./hash.py)
- Hash: `18f2048f7d4de5caabd2d0a3d23f4015af8033d46736a2e2d747b777a4d4d205`

## Solution
The python code is obfuscated:
```python
import base64, codecs
magic = 'IyEvdXNyL2Jpbi9weXRob24KIyAtKi0gY29kaW5nOiB1dGYtOCAtKi0KaW1wb3J0IHN5cwoKCgojIGZyb20gaHR0cHM6Ly9hc2VjdXJpdHlzaXRlLmNvbS9zdWJqZWN0cy9jaGFwdGVyODgKc2JveCA9IFsnMDExMDAwMTEnLCAnMDExMTExMDAnLCAnMDExMTAxMTEnLCAnMDExMTEwMTEnLCAnMTExMTAwMTAnLCAnMDExMDEwMTEnLCAnMDExMDExMTEnLCAnMTEwMDAxMDEnLCAnMDAxMTAwMDAnLCAnMDAwMDAwMDEnLCAnMDExMDAxMTEnLCAnMDAxMDEwMTEnLCAnMTExMTExMTAnLCAnMTEwMTAxMTEnLCAnMTAxMDEwMTEnLCAnMDExMTAxMTAnLCAnMTEwMDEwMTAnLCAnMTAwMDAwMTAnLCAnMTEwMDEwMDEnLCAnMDExMTExMDEnLCAnMTExMTEwMTAnLCAnMDEwMTEwMDEnLCAnMDEwMDAxMTEnLCAnMTExMTAwMDAnLCAnMTAxMDExMDEnLCAnMTEwMTAxMDAnLCAnMTAxMDAwMTAnLCAnMTAxMDExMTEnLCAnMTAwMTExMDAnLCAnMTAxMDAxMDAnLCAnMDExMTAwMTAnLCAnMTEwMDAwMDAnLCAnMTAxMTAxMTEnLCAnMTExMTExMDEnLCAnMTAwMTAwMTEnLCAnMDAxMDAxMTAnLCAnMDAxMTAxMTAnLCAnMDAxMTExMTEnLCAnMTExMTAxMTEnLCAnMTEwMDExMDAnLCAnMDAxMTAxMDAnLCAnMTAxMDAxMDEnLCAnMTExMDAxMDEnLCAnMTExMTAwMDEnLCAnMDExMTAwMDEnLCAnMTEwMTEwMDAnLCAnMDAxMTAwMDEnLCAnMDAwMTAxMDEnLCAnMDAwMDAxMDAnLCAnMTEwMDAxMTEnLCAnMDAxMDAwMTEnLCAnMTEwMDAwMTEnLCAnMDAwMTEwMDAnLCAnMTAwMTAxMTAnLCAnMDAwMDAxMDEnLCAnMTAwMTEwMTAnLCAnMDAwMDAxMTEnLCAnMDAwMTAwMTAnLCAnMTAwMDAwMDAnLCAnMTExMDAwMTAnLCAnMTExMDEwMTEnLCAnMDAxMDAxMTEnLCAnMTAxMTAwMTAnLCAnMDExMTAxMDEnLCAnMDAwMDEwMDEnLCAnMTAwMDAwMTEnLCAnMDAxMDExMDAnLCAnMDAwMTEwMTAnLCAnMDAwMTEwMTEnLCAnMDExMDExMTAnLCAnMDEwMTEwMTAnLCAnMTAxMDAwMDAnLCAnMDEwMTAwMTAnLCAnMDAxMTEwMTEnLCAnMTEwMTAxMTAnLCAnMTAxMTAwMTEnLCAnMDAxMDEwMDEnLCAnMTExMDAwMTEnLCAnMDAxMDExMTEnLCAnMTAwMDAxMDAnLCAnMDEwMTAwMTEnLCAnMTEwMTAwMDEnLCAnMDAwMDAwMDAnLCAnMTExMDExMDEnLCAnMDAxMDAwMDAnLCAnMTExMTExMDAnLCAnMTAxMTAwMDEnLCAnMDEwMTEwMTEnLCAnMDExMDEwMTAnLCAnMTEwMDEwMTEnLCAnMTAxMTExMTAnLCAnMDAxMTEwMDEnLCAnMDEwMDEwMTAnLCAnMDEwMDExMDAnLCAnMDEwMTEwMDAnLCAnMT'
love = 'RjZQRkZGRaYPNaZGRjZGNjZQNaYPNaZGRkZQRkZGRaYPNaZGNkZQRjZGNaYPNaZGRkZGRjZGRaYPNaZQRjZQNjZGRaYPNaZQRjZQRkZQRaYPNaZQNkZGNjZGRaYPNaZGNjZQNkZQRaYPNaZQRjZQNkZQRaYPNaZGRkZGRjZQRaYPNaZQNjZQNjZGNaYPNaZQRkZGRkZGRaYPNaZQRjZGNjZQNaYPNaZQNkZGRkZQNaYPNaZGNjZGRkZGRaYPNaZGNkZQRjZQNaYPNaZQRjZGNjZQRaYPNaZGNkZQNjZGRaYPNaZQRjZQNjZQNaYPNaZGNjZQRkZGRaYPNaZGNjZGNjZGNaYPNaZGNjZGRkZQRaYPNaZQNkZGRjZQNaYPNaZGRkZGNkZQRaYPNaZGNkZGRkZQNaYPNaZGNkZGNkZGNaYPNaZGRjZGRjZGNaYPNaZQNkZQNjZQRaYPNaZQNjZGNjZQNaYPNaZGRkZGRkZGRaYPNaZGRkZGNjZGRaYPNaZGRjZGNjZGNaYPNaZGRjZQRkZQRaYPNaZQNjZQRkZQNaYPNaZQNjZGNjZGRaYPNaZGRkZQRkZQNaYPNaZQRjZGRkZGRaYPNaZGNjZGNkZGRaYPNaZQRjZQNkZQNaYPNaZQNjZGNkZGRaYPNaZGRjZQNkZQNaYPNaZGNkZQNkZGRaYPNaZQRkZGRkZGNaYPNaZQNkZGRkZQRaYPNaZQRkZQNkZQNaYPNaZQRjZGRkZQRaYPNaZQNjZGRjZQRaYPNaZQRkZGNjZGRaYPNaZQRkZQNjZQNaYPNaZGNjZQNjZQRaYPNaZQRjZQRkZGRaYPNaZGRjZGRkZQNaYPNaZQNkZQNjZGNaYPNaZQNkZQRjZGNaYPNaZGNjZGNjZQNaYPNaZGNjZQRjZQNaYPNaZQRjZQNkZGNaYPNaZGRkZQRkZGNaYPNaZGNkZGRjZQNaYPNaZQNjZGNkZQNaYPNaZGRjZGRkZGNaYPNaZQRjZGRkZGNaYPNaZQNjZQRjZGRaYPNaZGRjZGRjZGRaYPNaZGRkZQNjZQNaYPNaZQNkZGNjZGNaYPNaZQNkZGRjZGNaYPNaZQNjZQRjZGNaYPNaZQRjZQRjZQRaYPNaZQNjZQNkZGNaYPNaZQNkZQNkZQNaYPNaZQRjZGRkZQNaYPNaZGRjZQNjZGNaYPNaZGRjZGNjZGRaYPNaZGNkZQRkZQNaYPNaZQRkZQNjZGNaYPNaZGNjZGNjZQRaYPNaZGNjZGNkZQRaYPNaZGRkZQNkZQNaYPNaZQRkZGRjZQRaYPNaZGRkZQNkZGRaYPNaZGRjZQRjZQNaYPNaZQNkZGNkZGRaYPNaZQRkZQRkZQRaYPNaZGNjZQRkZQRaYPNaZGRjZGNkZQRaYPNaZQRjZQRkZGNaYPNaZGNkZQRjZQRaYPNaZQRkZQRkZQNaYPNaZQRjZGNkZGNaYPNaZGRkZGNkZQNaYPNaZGRkZQRjZGNaYPNaZQRkZQNkZQRaYPNaZQRkZGRjZGNaYPNaZGNkZQRkZGNaYPNaZQNjZQRjZQNaYPNaZGNkZGRjZGNaYPNaZQRkZGRjZQNaYPNaZQNkZQNkZQRaYPNaZQNkZQRkZGNaYPNaZQNjZGRkZQNaYPNaZGNkZQNkZGNaYPNaZGNkZGNkZQNaYPNaZGRjZQNkZGNaYPNa'
god = 'MTExMDEwMDAnLCAnMTEwMTExMDEnLCAnMDExMTAxMDAnLCAnMDAwMTExMTEnLCAnMDEwMDEwMTEnLCAnMTAxMTExMDEnLCAnMTAwMDEwMTEnLCAnMTAwMDEwMTAnLCAnMDExMTAwMDAnLCAnMDAxMTExMTAnLCAnMTAxMTAxMDEnLCAnMDExMDAxMTAnLCAnMDEwMDEwMDAnLCAnMDAwMDAwMTEnLCAnMTExMTAxMTAnLCAnMDAwMDExMTAnLCAnMDExMDAwMDEnLCAnMDAxMTAxMDEnLCAnMDEwMTAxMTEnLCAnMTAxMTEwMDEnLCAnMTAwMDAxMTAnLCAnMTEwMDAwMDEnLCAnMDAwMTExMDEnLCAnMTAwMTExMTAnLCAnMTExMDAwMDEnLCAnMTExMTEwMDAnLCAnMTAwMTEwMDAnLCAnMDAwMTAwMDEnLCAnMDExMDEwMDEnLCAnMTEwMTEwMDEnLCAnMTAwMDExMTAnLCAnMTAwMTAxMDAnLCAnMTAwMTEwMTEnLCAnMDAwMTExMTAnLCAnMTAwMDAxMTEnLCAnMTExMDEwMDEnLCAnMTEwMDExMTAnLCAnMDEwMTAxMDEnLCAnMDAxMDEwMDAnLCAnMTEwMTExMTEnLCAnMTAwMDExMDAnLCAnMTAxMDAwMDEnLCAnMTAwMDEwMDEnLCAnMDAwMDExMDEnLCAnMTAxMTExMTEnLCAnMTExMDAxMTAnLCAnMDEwMDAwMTAnLCAnMDExMDEwMDAnLCAnMDEwMDAwMDEnLCAnMTAwMTEwMDEnLCAnMDAxMDExMDEnLCAnMDAwMDExMTEnLCAnMTAxMTAwMDAnLCAnMDEwMTAxMDAnLCAnMTAxMTEwMTEnLCAnMDAwMTAxMTAnXQoKCgoKZGVmIHN0cmluZzJiaXRzKHM9JycpOgogICAgdG1wID0gW10KICAgIGZvciB4IGluIHMgOgogICAgICAgIGJ5dGUgPSBiaW4ob3JkKHgpKVsyOl0KICAgICAgICBpZiBsZW4oYnl0ZSkgPiA4OgogICAgICAgICAgICBpbmRpY2VzID0gW2kgZm9yIGkgaW4gcmFuZ2UoMCwgbGVuKGJ5dGUpLCA4KV0KICAgICAgICAgICAgcGFydHMgPSBbIiIuam9pbihieXRlW2k6al0pLnpmaWxsKDgpIGZvciBpLGogaW4gemlwKGluZGljZXMsIGluZGljZXNbMTpdK1tOb25lXSldCiAgICAgICAgICAgIHRtcCArPSAocGFydHMpCiAgICAgICAgZWxzZSA6CiAgICAgICAgICAgIGJ5dGUgPSBieXRlLnpmaWxsKDgpCiAgICAgICAgICAgIHRtcC5hcHBlbmQoYnl0ZSkKICAgIHJldHVybiB0bXAKCmRlZiBwYWRkaW5nKGJpbmFyeSk6CiAgICBpZigobGVuKGJpbmFyeSkgKyAxICkgJSAzMiA9PSAwKToKICAgICAgICBiaW5hcnkuYXBwZW5kKCcwMDAwMDAwMScpCiAgICAgICAgYmluYXJ5LmFwcGVuZCgnMDAwMDAwMDAnKQogICAgaWYobGVuKGJpbmFyeSklMzIgIT0gMCBvciBsZW4oYmluYXJ5KSA9PSAwKToKICAgICAgICBiaW5hcnkuYXBwZW5kKCcwMD'
destiny = 'NjZQNjZFpcPvNtVPNtVPNtq2ucoTHtoTIhXTWcozSlrFxyZmVtVG0tZQbXVPNtVPNtVPNtVPNtLzyhLKW5YzSjpTIhMPtaZQNjZQNjZQNaXDbXMTIzVUuipvuuYTVcBtbtVPNtpzImVQ0tVvVXVPNtVTMipvOcVTyhVUWuozqyXTkyovuuXFx6PvNtVPNtVPNtVPNtVUWyplNeCFOmqUVbnJ50XTSonI0cVS4tnJ50XTWonI0cXDbtVPNtpzI0qKWhVUWypjbXMTIzVUAvo3uso3OyXTWcozSlrFx6PvNtVPOzo3VtnFOcovOlLJ5aMFufMJ4bLzyhLKW5XFx6PvNtVPNtVPNtnJ5xMKttCFOcoaDbLzyhLKW5J2yqYQVcPvNtVPNtVPNtLzyhLKW5J2yqVQ0tp2WirSgcozEyrS0XPzEyMvOjnTSmMGRbLzyhLKW5XGbXVPNtVT0tCFOcoaDboTIhXTWcozSlrFxtYlNmZvxXVPNtVUEgpPN9VSgqPvNtVPOzo3VtnFOcovOlLJ5aMFtjYPOfMJ4bLzyhLKW5XFjtoFx6PvNtVPNtVPNtqT1jYzSjpTIhMPu4o3VbLzyhLKW5J2yqYPOvnJ5upayonFfkKFxcPvNtVPOlMKE1pz4tqT1jPtcxMJLtpTuup2HlXTWcozSlrFx6PvNtVPOzo3VtnFOcovOlLJ5aMFtkYTkyovuvnJ5upaxcXGbXVPNtVPNtVPOzo3VtnvOcovOlLJ5aMFucXGbXVPNtVPNtVPNtVPNtLzyhLKW5J2yqVQ0trT9lXTWcozSlrIgcKFjtLzyhLKW5J2cqXDbXMTIzVTWcqUZlnTI4XTWcozSlrFx6PvNtVPObMKusp3ElVQ0tVvVXVPNtVTMipvOvnKDtnJ4tLzyhLKW5BtbtVPNtVPNtVTuyrS9mqUVtXm0tMz9loJS0XTyhqPuvnKDfVQVcYPNaZQW4WlxXVPNtVUWyqUIlovObMKusp3ElPtcxMJLtnPugXGbXVPNtVUOfLJyhVQ0toDbtVPNtLzyhLKW5VQ0tp3ElnJ5aZzWcqUZbpTkunJ4cPvNtVPOjLJExnJ5aXTWcozSlrFxXVPNtVTyzVTkyovuvnJ5upaxcVQ4tZmV6PvNtVPNtVPNtLzyhLKW5VQ0tpTuup2HkXTWcozSlrFxXVPNtVUObLKAyZvuvnJ5upaxcPvNtVPOjnTSmMGVbLzyhLKW5XDbtVPNtpTuup2HlXTWcozSlrFxXVPNtVUAvo3uso3OyXTWcozSlrFxXVPNtVTuup2usp3ElVQ0tLzy0pmWbMKtbLzyhLKW5XDbtVPNtpzI0qKWhVTuup2usp3ElPtbXpTkunJ4tCFNtVvVXnJLtoTIhXUA5pl5upzq2XFN9CFNkBtbtVPNtpUWcoaDbVxS1L3IhVTSlM3IgMJ50VTEioz7QdF4tHzyyovQQbPObLJAbMKVhVRW5MFOvrJHhVvxXMJkcMvOfMJ4bp3ymYzSlM3LcVQ49VQVtBtbtVPNtpTkunJ4tXm0tp3ymYzSlM3MoZI0XVPNtVTMipvOcVTyhVUWuozqyXQVfoTIhXUA5pl5upzq2XFx6PvNtVPNtVPNtpTkunJ4tXm0tVvNvVPftp3ElXUA5pl5upzq2J2yqXDbtVPNtpUWcoaDbnPujoTScovxcPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
```

But we can simply replace the last line `eval` by a `print` to get the deobfuscated code instead of evaluating it:
```python
print(base64.b64decode(eval('\x74\x72\x75\x73\x74')).decode())
```

Output file is stored in [trust.py](./trust.py):
```console
python3 hash.py > trust.py
```

The hashing algorithm mainly uses two phases `phase1()` and `phase2()` (which is run multiple times), and a `sbox_str()` which refers to [AES encryption](https://asecuritysite.com/subjects/chapter88). We'll have to revert all three:

```python
def h(m):
    plain = m
    binary = string2bits(plain)
    padding(binary)
    if len(binary) > 32:
        binary = phase1(binary)
    phase2(binary)
    phase2(binary)
    phase2(binary)
    sbox_ope(binary)
    hash_str = bits2hex(binary)
    return hash_str
```

Let's start reverting `sbox_ope()` first. In same post [AES encryption](https://asecuritysite.com/subjects/chapter88), we get the `inverse S-box`, in hexadecimal. We just have to translate the values in binary format using this piece of code:
```python
# from https://asecuritysite.com/subjects/chapter88
sbox_inv = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]

s = []
for x in sbox_inv:
    s.append(format(x, '08b'))
print(s)
```

This gives us the inverse S-box in binary format:
```console
$ python3 inv.py
['01010010', '00001001', '01101010', '11010101', '00110000', '00110110', '10100101', '00111000', '10111111', '01000000', '10100011', '10011110', '10000001', '11110011', '11010111', '11111011', '01111100', '11100011', '00111001', '10000010', '10011011', '00101111', '11111111', '10000111', '00110100', '10001110', '01000011', '01000100', '11000100', '11011110', '11101001', '11001011', '01010100', '01111011', '10010100', '00110010', '10100110', '11000010', '00100011', '00111101', '11101110', '01001100', '10010101', '00001011', '01000010', '11111010', '11000011', '01001110', '00001000', '00101110', '10100001', '01100110', '00101000', '11011001', '00100100', '10110010', '01110110', '01011011', '10100010', '01001001', '01101101', '10001011', '11010001', '00100101', '01110010', '11111000', '11110110', '01100100', '10000110', '01101000', '10011000', '00010110', '11010100', '10100100', '01011100', '11001100', '01011101', '01100101', '10110110', '10010010', '01101100', '01110000', '01001000', '01010000', '11111101', '11101101', '10111001', '11011010', '01011110', '00010101', '01000110', '01010111', '10100111', '10001101', '10011101', '10000100', '10010000', '11011000', '10101011', '00000000', '10001100', '10111100', '11010011', '00001010', '11110111', '11100100', '01011000', '00000101', '10111000', '10110011', '01000101', '00000110', '11010000', '00101100', '00011110', '10001111', '11001010', '00111111', '00001111', '00000010', '11000001', '10101111', '10111101', '00000011', '00000001', '00010011', '10001010', '01101011', '00111010', '10010001', '00010001', '01000001', '01001111', '01100111', '11011100', '11101010', '10010111', '11110010', '11001111', '11001110', '11110000', '10110100', '11100110', '01110011', '10010110', '10101100', '01110100', '00100010', '11100111', '10101101', '00110101', '10000101', '11100010', '11111001', '00110111', '11101000', '00011100', '01110101', '11011111', '01101110', '01000111', '11110001', '00011010', '01110001', '00011101', '00101001', '11000101', '10001001', '01101111', '10110111', '01100010', '00001110', '10101010', '00011000', '10111110', '00011011', '11111100', '01010110', '00111110', '01001011', '11000110', '11010010', '01111001', '00100000', '10011010', '11011011', '11000000', '11111110', '01111000', '11001101', '01011010', '11110100', '00011111', '11011101', '10101000', '00110011', '10001000', '00000111', '11000111', '00110001', '10110001', '00010010', '00010000', '01011001', '00100111', '10000000', '11101100', '01011111', '01100000', '01010001', '01111111', '10101001', '00011001', '10110101', '01001010', '00001101', '00101101', '11100101', '01111010', '10011111', '10010011', '11001001', '10011100', '11101111', '10100000', '11100000', '00111011', '01001101', '10101110', '00101010', '11110101', '10110000', '11001000', '11101011', '10111011', '00111100', '10000011', '01010011', '10011001', '01100001', '00010111', '00101011', '00000100', '01111110', '10111010', '01110111', '11010110', '00100110', '11100001', '01101001', '00010100', '01100011', '01010101', '00100001', '00001100', '01111101']
```

We'll use the inverse S-box as follow:
```python
def sbox_ope_inv(binary):
    for i in range(len(binary)):
        index = int(binary[i], 2)
        binary[i] = sbox_inv[index]
```

Next, let's look at `phase1()`. It is XORing blocks of 32 bytes. Since the hash we're given is 32 bytes long, `phase1()` is doing nothing to our hash and we can skip it:
```python
def phase1(binary):
    m = int(len(binary) / 32)
    tmp = []
    for i in range(0, len(binary), m):
        tmp.append(xor(binary[i], binary[i+1]))
    return tmp
```

So we're left with reverting `phase2()`, which is reverted by doing the XOR operations in reverse order::
```python
def phase2(binary):
    for i in range(1,len(binary)):
        for j in range(i):
            binary[i] = xor(binary[i], binary[j])
```

```python
def phase2_inv(binary):
    for i in reversed(range(1,len(binary))):
        for j in reversed(range(i)):
            binary[i] = xor(binary[i], binary[j])
```

In the end, the reverse hashing function is as follow, where `hex2bits` is a helper function to convert the hash in hexadecimal into binary:
```python
def h_inv(hash_str):
    binary = hex2bits(hash_str)
    sbox_ope_inv(binary)
    phase2_inv(binary)
    phase2_inv(binary)
    phase2_inv(binary)
    print(''.join([chr(int(x, 2)) for x in binary]))
```


The complete solution is given in [sol.py](./sol.py).
```console
$ python3 sol.py
404CTF{yJ7dhDm35pLoJcbQkUygIJ}
```

## Python code
Complete solution in [sol.py](./sol.py)

## Flag
404CTF{yJ7dhDm35pLoJcbQkUygIJ}
