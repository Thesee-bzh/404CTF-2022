# Retro / Mise à jour requise

## Challenge
Notre service de renseignement nous a informé qu'un agent de Hallebarde avait une curieuse façon de gérer la sécurité de ses fichiers. Il semblerait qu'il s'agisse d'un fan inconditionnel de Python au point de l'utiliser pour gérer ses mots de passe! Nous avons réussi à intercepter une partie du code source qui gère la vérification du mot de passe maître.

Votre mission est de trouver ce mot de passe. Attention cependant, il semblerait que notre pythonesque ami ait utilisé des syntaxes spécifiques à Python3.10, j'espère que cela ne vous posera pas de problèmes!

Bonne chance à vous!

## Inputs
- Python code to reverse: [chall.py](./chall.py)

## Solution
We need to reverse three functions to decrypt the encoded secret:
```python
if c(b(input("password:"), 1)):
    print("Utilise ce mot de passe pour valider le challenge!")
```

First function `a()` takes an ASCII character as input, is recursive and makes use of randomly selected numbers (see imported mobule `random`). Those are seeded once (based on the value of the input character), when the function is called from other code (but not from `a()` itself).
```python
def a(c, r=True):
    n = ord(c)
    if r: rd.seed(n)
    match n:
        case 0:
            return dict.fromkeys(range(10), 0)
        case _:
            return (d:=a(chr(n - 1), False)) | {(m:=rd.randint(0, 9)): d[m] + rd.randint(0,2)}
```

What we can do is to compute the output of `a()` for every ASCII character, store the result in a static list `REV_A` and use `REV_A.index(x)` to revert `a()`:
```python
print("REV_A = [")
for i in range(256):
    print("    ", list(a(chr(i)).values()), ",")
print("]")
```

```python
REV_A = [
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ,
     [0, 0, 2, 0, 0, 0, 0, 0, 0, 0] ,
     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0] ,
     [0, 0, 0, 2, 0, 2, 0, 0, 0, 0] ,
     [0, 2, 0, 1, 0, 0, 1, 0, 0, 0] ,
     # (..)
     [23, 18, 30, 22, 26, 31, 35, 34, 21, 35] ,
     [26, 16, 31, 18, 21, 35, 23, 28, 25, 12] ,
     [30, 21, 29, 25, 37, 31, 18, 23, 26, 32] ,
]
```

We can do about the same with third function `c()`, which is also recursive and also makes use of randomly selected numbers. Those are seeded based on static list `s`.
```python
def c(p, n=0):
    match p:
        case []:
            return n!=0
        case [f, *rest]:
            rd.seed(s[n])
            return rd.randint(0,30) == f and c(rest, n + 1)
```

So let's compute a static list `REV_C` (we'll use `REV_C.index(x)` to revert `c()`):
```python
rev_c = []
for n in range(len(s)):
    rd.seed(s[n])
    rev_c.append(rd.randint(0,30))
print("REV_C = ", rev_c)
```

```python
REV_C =  [11, 7, 15, 14, 4, 9, 4, 7, 3, 6, 8, 11, 11, 4, 14, 8, 7, 6, 9, 11, 11, 4, 9, 10, 6, 8, 7, 8, 5, 7, 8, 12, 3, 7, 4, 3, 9, 8, 2, 8, 7, 6, 11, 5, 5, 7, 1, 11, 5, 7, 4, 1, 5, 11, 8, 11, 4, 7, 4, 11, 8, 5, 9, 11, 7, 7, 3, 5, 8, 3, 11, 5, 10, 7, 10, 12, 10, 10, 8, 8, 8, 7, 9, 4, 7, 8, 4, 12, 5, 11, 2, 11, 9, 4, 10, 13, 5, 6, 6, 6, 9, 7, 4, 9, 7, 11, 8, 8, 3, 4, 7, 6, 6, 0, 2, 6, 2, 5, 6, 7, 8, 2, 9, 10, 10, 6, 3, 7, 5, 3, 9, 6, 5, 10, 4, 2, 8, 7, 3, 6, 6, 10, 4, 4, 8, 17, 9, 8, 6, 3, 3, 11, 9, 4, 7, 13, 3, 7, 4, 4, 4, 6, 8, 3, 6, 5, 7, 10, 8, 6, 2, 4, 1, 4, 11, 4, 7, 5, 3, 12, 2, 10, 8, 6, 10, 4, 7, 9, 8, 8, 10, 5, 4, 7, 5, 4, 9, 10, 4, 6, 3, 7, 6, 10, 0, 4, 10, 5, 10, 2, 7, 7, 3, 2, 3, 4, 2, 15, 5, 0, 6, 4, 8, 8, 1, 13, 2, 7, 2, 9, 3, 9, 9, 10, 7, 4, 7, 7, 3, 4, 9, 11, 13, 7, 4, 2, 8, 19, 11, 6, 7, 9, 10, 3, 7, 8, 10, 0, 8, 6, 14, 7, 13, 8, 11, 3, 5, 5, 7, 10, 7, 7, 7, 10, 7, 7, 11, 6, 7, 7, 8, 2, 8, 7, 5, 10, 18, 7, 5, 4, 10, 10, 5, 8, 1, 5, 7, 2, 6, 2, 8, 4, 5, 18, 4, 2, 4, 11, 2, 7, 13, 7, 5, 4, 4, 4, 11, 5, 12, 9, 4, 6, 4, 5, 9, 11, 4, 10, 7, 8, 11, 5, 6, 3, 10, 3, 7, 3, 8, 10, 11, 18, 5, 8, 7, 11, 8, 7, 2, 1, 8, 3, 4, 8, 4, 3, 5, 9, 10, 7, 10, 0, 4, 5, 23, 10, 7, 7, 2, 4, 10, 5, 10, 4, 11, 5, 6, 3, 10, 7]
```

Last function `b()` is recursive as well and shuffles a temporary list using `rd.shuffle()` from module `random`:
```python
def b(p, n):
    match list(p):
        case []:
            return []
        case [f, *rest]:
            l = list(a(f).values()) + b(''.join(rest), n*2)
            rd.seed(n)
            rd.shuffle(l)
            return l
```

So we need a way to `unshuffle` a shuffled list listed with some seed, like so for instance:
```python
# Unshuffle list 'l' seeded with 's'
def unshuffle(l, s):
    order = list(range(len(l)))
    rd.seed(s)
    rd.shuffle(order)
    l_ = [0]*len(l)
    for i, i_ in enumerate(order):
        l_[i_] = l[i]
    return l_
```

Here is how I reverted function `b()`:
```python
# Invert b()
def r_b(l, n):
    match l:
        case []:
            return []
        case _:
            l_ = unshuffle(l, n)
            c = REV_A.index(l_[0: 10])
            return [chr(c)] + r_b(l_[10::], 2*n)
```

We put that together to get the flag:
```python
print(''.join([x for x in r_b(REV_C, 1)]))
```

## Python code
Complete solution in [sol.py](./sol.py)

## Flag
404CTF{M3RC1_PY7H0N3.10_P0UR_L3_M47CH}
