# Retro / Renverse la tour ! [1/2]

## Challenge
Nos experts ont réussi à mettre la main sur un algorithme d'authentification ultra secret utilisé par notre ennemi !

Un unique mot de passe est accepté mais nous n'avons pas pu le recupérer. Pouvez-vous nous aider ?

## Inputs
- Python code to reverse: [reverse1.py](./reverse1.py)

## Solution
We need to reverse three function to decrypt the encoded secret:
```python
if tour3(tour2(tour1(mdp))) == "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5":
    print("Bravo ! Le flag est 404CTF{" + mdp + "}")
```

First function simply reverts the input string and return a list of the corresponding ASCII decimal values:
```python
def tour1(password):
    string = str("".join( "".join(password[::-1])[::-1])[::-1])
    return [ord(c) for c in string]
```

So we easily revert it like so (just using lists):
```python
def r_tour1(password):
    return password[::-1]
```

Second function is as follow. Variable `i` is always 0.
```python
def tour2(password):
    new = []
    i = 0
    while password != []:
        new.append(password[password.index(password[i])])
        new.append(password[password.index(password[i])] + password[password.index(password[ i + 1 %len(password)])])
        password.pop(password.index(password[i]))
        i += int('qkdj', base=27) - int('QKDJ', base=31) + 267500
    return new
```

So it takes a list of ASCII decimal values and returns a list twice as long, where inserted elements are the sum of the two preceeding values in the input list. Example: with input list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, `tour2()` returns `[1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6, 13, 7, 15, 8, 17, 9, 19, 10, 20]`.

This is again easily reverted by dropping one element on two like so:
```python
def r_tour2(password):
    return password[0::2]
```

Third function starts with a static list of chars, that is modified based on the given input:
```python
def tour3(password):
    mdp =['l', 'x', 'i', 'b', 'i', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j', 'o', 'r', 'y', 'r', 'u', 'a']
    for i in range(len(password)):
        mdp[i], mdp[len(password) - i -1 ] = chr(password[len(password) - i -1 ] + i % 4),  chr(password[i] + i % 4)
    return "".join(mdp)
```

Reverted code:
```python
def r_tour3(password):
    mdp = ['l', 'x', 'i', 'b', 'i', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j', 'o', 'r', 'y', 'r', 'u', 'a']
    for i in range(len(password)):
        mdp[i] = ord(password[len(password) - i -1 ]) - i % 4
        mdp[len(password) - i -1 ] = ord(password[i]) - i % 4
    return mdp
```

We put that together to get the decoded password:
```python
ENC_PWD = "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5"
mdp_ = r_tour1(r_tour2(r_tour3(ENC_PWD)))
print(''.join([chr(x) for x in mdp_]))
```

```console
$ python3 sol.py
P4sS1R0bUst3Qu3C4
```

Before submitting the flag, we can check this is the correct password using the input python code:
```console
$ python3 reverse1.py
Mot de passe : P4sS1R0bUst3Qu3C4
Bravo ! Le flag est 404CTF{P4sS1R0bUst3Qu3C4}
```

## Python code
Complete solution in [sol.py](./sol.py)

## Flag
404CTF{P4sS1R0bUst3Qu3C4}
