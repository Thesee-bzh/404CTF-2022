# Retro / Pas de mise à jour

## Challenge :star:
Le fan de Python de Hallebarde est de retour! Mais il ne veut plus que tout le monde puisse lire ses codes sources...

## Inputs
- Compiled Python bytecode: [chall.pyc](./chall.pyc)

## Solution
Decompilation with `uncompyle6` fails because of unsupported Python version 3.10.0:
```console
$ uncompyle6 chall.pyc
# uncompyle6 version 3.8.0
# Python bytecode 3.10.0 (3439)
# Decompiled from: Python 3.10.4 (main, Mar 24 2022, 13:07:27) [GCC 11.2.0]
# Embedded file name: /tmp/chall.py
# Compiled at: 2022-05-08 13:17:43
# Size of source mod 2**32: 507 bytes

Unsupported Python version, 3.10.0, for decompilation


# Unsupported bytecode in file chall.pyc
# Unsupported Python version, 3.10.0, for decompilation
```

Looking for another decompilation tool, I found out `xdis` at https://pypi.org/project/xdis/, which provides the `pydisasm` binary:
```console
$ pip install xdis
$ pydisasm chall.pyc > chall.pyasm
```

Now we have the decompiled bytecode in [chall.pyasm](./chall.pyasm). Here is the beginning:
```console
$ head -50 chall.pyasm
# pydisasm version 6.0.4
# Python bytecode 3.10.0 (3439)
# Disassembled from Python 3.10.4 (main, Mar 24 2022, 13:07:27) [GCC 11.2.0]
# Timestamp in code: 1652008663 (2022-05-08 13:17:43)
# Source code size mod 2**32: 507 bytes
# Method Name:       <module>
# Filename:          /tmp/chall.py
# Argument count:    0
# Position-only argument count: 0
# Keyword-only arguments: 0
# Number of locals:  0
# Stack size:        3
# Flags:             0x00000040 (NOFREE)
# First Line:        1
# Constants:
#    0: <code object <listcomp> at 0x7f702d4e5e70, file "/tmp/chall.py", line 3>
#    1: '<listcomp>'
#    2: 'Password:'
#    3: 'd1j#H(&Ja1_2 61fG&'
#    4: <code object code at 0x7f702d4e5f20, file "/tmp/chall.py", line 7>
#    5: 'code'
#    6: (292, 194, 347, 382, 453, 276, 577, 434, 183, 295, 318, 196, 482, 325, 412, 502, 396, 402, 328, 194, 473, \
490, 299, 503, 386, 215, 263, 211, 318, 206, 533)
#    7: 'Bravo!'
#    8: 'Dommage...'
#    9: None
# Names:
#    0: input
#    1: userInput
#    2: key
#    3: code
#    4: print
  3:           0 LOAD_CONST           (<code object <listcomp> at 0x7f702d4e5e70, file "/tmp/chall.py", line 3>)
               2 LOAD_CONST           ('<listcomp>')
               4 MAKE_FUNCTION        (Neither defaults, keyword-only args, annotations, nor closures)
               6 LOAD_NAME            (input)
               8 LOAD_CONST           ('Password:')
              10 CALL_FUNCTION        1
              12 GET_ITER
              14 CALL_FUNCTION        1
              16 STORE_NAME           (userInput)

  4:          18 LOAD_CONST           ('d1j#H(&Ja1_2 61fG&')
              20 STORE_NAME           (key)

  7:          22 LOAD_CONST           (<code object code at 0x7f702d4e5f20, file "/tmp/chall.py", line 7>)
              24 LOAD_CONST           ('code')
              26 MAKE_FUNCTION        (Neither defaults, keyword-only args, annotations, nor closures)
              28 STORE_NAME           (code)

 14:          30 LOAD_NAME            (code)

```

So now we can reverse the bytecode as we did in the other challenges. Here is the python code after reversing, in [chall.py](./chall.py):
```python
userinput = [ord(e) for e in input('Password:')]
key = 'd1j#H(&Ja1_2 61fG&'

def code(l):
    match l:
        case [el, *rest]:
            return [5*el ^ ord(key[len(rest) % len(key)])] + code(rest)
        case []:
            return []

if code(userinput) == [292, 194, 347, 382, 453, 276, 577, 434, 183, 295, 318, 196, 482, 325, 412, 502, 396, 402, 328, 194, 473, 490, 299, 503, 386, 215, 263, 211, 318, 206, 533]:
    print('Bravo!')
else:
    print('Dommage...')
```

Final step is to reverse the Python code itself, essentially the recursive function `code()` leading to list [292, 194, 347, 382, 453, 276, 577, 434, 183, 295, 318, 196, 482, 325, 412, 502, 396, 402, 328, 194, 473, 490, 299, 503, 386, 215, 263, 211, 318, 206, 533]. Here is the reversed Python code in [sol.py](./sol.py):
```python
key = 'd1j#H(&Ja1_2 61fG&'
exp = [292, 194, 347, 382, 453, 276, 577, 434, 183, 295, 318, 196, 482, 325, 412, 502, 396, 402, 328, 194, 473, 490, 299, 503, 386, 215, 263, 211, 318, 206, 533]

def decode(l):
    match l:
        case [el, *rest]:
            return [(el ^ ord(key[len(rest) % len(key)])) // 5] + decode(rest)
        case []:
            return []

print(''.join([chr(x) for x in decode(exp)]))
```

Run it and we get the flag:
```console
$ python3 sol.py
404CTF{R34D1NG_PYTH0N_BYT3C0D3}

```

## Python code
Complete solution in [sol.py](./sol.py)

## Flag
404CTF{R34D1NG_PYTH0N_BYT3C0D3}
