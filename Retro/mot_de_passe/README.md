# Retro / Mot de passe

## Challenge
Nous avons retrouvé un petit ordinateur avec un drôle de programme pour chiffrer le mot de passe administrateur. Ta mission est simple : déchiffrer ce mot de passe !

## Inputs
- [Mdp.class](./Mdp.class)

## Solution
This is a some compiled `Java` class:
```console
$ file Mdp.class
Mdp.class: compiled Java class data, version 60.0
```

Let's use `jadx` to decompile `Mdp.class`
```console
$ jadx -d out ./Mdp.class
INFO  - loading ...
INFO  - processing ...
INFO  - done
```

The decompilation shows the source code in `Mdp.java`:
```console
$ find .
.
./out
./out/sources
./out/sources/chall
./out/sources/chall/Mdp.java
./Mdp.class
```

Here is [Mdp.java](./Mdp.java), where we see:
- the encoded secret `"4/2@PAu<+ViNgg%^5NS`#J\u001fNK<XNW(_"`
- the encding function `hide()`, which we need to revert.


Here is the source code for function `hide()`:
```java
    static String hide(String str) {
        String str2 = "";
        for (int i = 0; i < str.length(); i++) {
            str2 = str2 + ((char) (((char) (str.charAt(i) - i)) % 128));
        }
        return str2;
    }
```

And we revert it with some python code like so, to get the secret/flag:
```python
s = '4/2@PAu<+ViNgg%^5NS`#J\u001fNK<XNW(_'
p = ''.join([chr(ord(s[i]) + i) for i in range(len(s))])
print(p)
```

```console
$ python3 sol.py
404CTF{C3_sYst3mE_es7_5ecUrisE}
```

## Python code
Complete solution in [sol.py](./sol.py)

## Flag
404CTF{C3_sYst3mE_es7_5ecUrisE}
