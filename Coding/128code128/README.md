# Coding / 128code128

## Challenge
Nous avons envoyé un agent infiltrer un entrepôt suspect. Hélas le voilà désormais bloqué dans un dédale de portes ! Il semblerait que ces portes ne s'ouvrent qu'avec un code étrange que seuls les robots tueurs patrouillant dans le secteur semblent capables de déchiffrer... Heureusement, cet agent est en contact avec vous ! Aidez-le à décoder ces images et à ouvrir les portes pour qu'il puisse s'échapper ! Attention, si vous êtes trop lent ou que vous faites la moindre erreur, l'alarme retentira... Bonne chance !

## Inputs
- server: `challenge.404ctf.fr:30566`

## Solution
When we connect to the server, we're given some base64. We also see a counter that suggests that we'll have to iterate it 128 times...
```console
[0/128] Il paraît qu'il y a un mot de passe dans cette image... Peux-tu m'aider ? Vite vite vite !!!
iVBORw0KGgoAAAANSUhEUgAAAG4AAABkCAIAAADoopLKAAABH0lEQVR4nO3QMQ7DIBAAwVP+/2fSIWQcKcWUO9UJY0A7MzMza6211jns9XPDuWfPj5XXxfvYe/PjovvHX5f+8/LX9fvl96d7eJyw588EKSVTSqaUTCmZUjKlZErJlJIpJVNKppRMKZlSMqVkSsmUkiklU0qmlEwpmVIypWRKyZSSKSVTSqaUTCmZUjKlZErJlJIpJVNKppRMKZlSMqVkSsmUkiklU0qmlEwpmVIypWRKyZSSKSVTSqaUTCmZUjKlZErJlJIpJVNKppRMKZlSMqVkSsmUkiklU0qmlEwpmVIypWRKyZSSKSVTSqaUTCmZUjKlZErJlJIpJVNKppRMKZlSMqVkSsmUkiklU0qmlEwpmVIypWRKyZSSKSVTSuYLQYauGbBb3YAAAAAASUVORK5CYII=
>>
```

When we `base64` decode it, we end up with a `PNG` file:
```console
$ echo -n iVBORw0KGgoAAAANSUhEUgAAAG4AAABkCAIAAADoopLKAAABH0lEQVR4nO3QMQ7DIBAAwVP+/2fSIWQcKcWUO9UJY0A7MzMza6211jns9XPDuWfPj5XXxfvYe/PjovvHX5f+8/LX9fvl96d7eJyw588EKSVTSqaUTCmZUjKlZErJlJIpJVNKppRMKZlSMqVkSsmUkiklU0qmlEwpmVIypWRKyZSSKSVTSqaUTCmZUjKlZErJlJIpJVNKppRMKZlSMqVkSsmUkiklU0qmlEwpmVIypWRKyZSSKSVTSqaUTCmZUjKlZErJlJIpJVNKppRMKZlSMqVkSsmUkiklU0qmlEwpmVIypWRKyZSSKSVTSqaUTCmZUjKlZErJlJIpJVNKppRMKZlSMqVkSsmUkiklU0qmlEwpmVIypWRKyZSSKSVTSuYLQYauGbBb3YAAAAAASUVORK5CYII=| base64 -d > 0.png
```

This is a a bar code, hence the format `code 128`:
![0.png](./0.png)

There, I spent some time trying to decode it unsuccesfully, before realizing the bar code is truncated: it doesn't contain the `start code`, nor the `end code`, not even the `checksum`, but just the raw data. So we can't use existing library and need to decode it manually. To do that, we'll simply read the first line of the image (since the bar codes are always vertical), assuming:
- one bit per pixel
- black is 1, white is 0

Here we've already grabbed the `base64` blob and decoded it into `data`. We open the data as an image, read the fist line and build a list or zeros ans ones:
```python
BLACK = (0, 0, 0)

# Open the image, get width, read 1st line of pixels
# Translate 1st line in binary (1=Black, 0=White)
i = Image.open(io.BytesIO(data))
p = list(i.getdata())[0:i.size[0]]
b = ''.join(['1' if x == BLACK else '0' for x in p])
```

Then we count the number of consecutive zeros and ones, such that for instance `11011001100` translates into `212222`. The result is a `code 128` string, corresponding to the first line of the `PNG` file:
```python
# Convert in code128 string
code128 = ''
cur = ''
count = 0
for new in b:
    if new != cur and count != 0:
        code128 += str(count)
        count = 1
    else:
        count += 1
    cur = new
code128 += str(count)
```

Then we split the `code 128` string into a list of `code 128` codes, which we revert to ASCII thanks to [Code 128](https://fr.wikipedia.org/wiki/Code_128):
```python
# Code128 symbols
# Starts with: (espace, ascii=32, code128=212222)
OFFSET = 32
CODE = ('212222', '222122', '222221', '121223', '121322', '131222', '122213', '122312', '132212', '221213', '221312', '231212', '112232', '122132', '122231', '113222', '123122', '123221', '223211', '221132', '221231', '213212', '223112', '312131', '311222', '321122', '321221', '312212', '322112', '322211', '212123', '212321', '232121', '111323', '131123', '131321', '112313', '132113', '132311', '211313', '231113', '231311', '112133', '112331', '132131', '113123', '113321', '133121', '313121', '211331', '231131', '213113', '213311', '213131', '311123', '311321', '331121', '312113', '312311', '332111', '314111', '221411', '431111', '111224', '111422', '121124', '121421', '141122', '141221', '112214', '112412', '122114', '122411', '142112', '142211', '241211', '221114', '413111', '241112', '134111', '111242', '121142', '121241', '114212', '124112', '124211', '411212', '421112', '421211', '212141', '214121', '412121', '111143', '111341', '131141')

# Break code128 string into code128 characters
# Revert to ASCII string
l = [code128[x:x+6] for x in range(0, len(code128), 6)]
s = ''.join([chr(CODE.index(x) + OFFSET) for x in l]).encode()
```

Last thing to do is to send it to the server and iterate 128 times. The interaction with the server is implemented using `pwntools`. Complete code in [sol.py](./sol.py).

```console
$ python3 sol.py
(...)
[125/128] Il paraît qu'il y a un mot de passe dans cette image... Peux-tu m'aider ? Vite vite vite !!!

b'iVBORw0KGgoAAAANSUhEUgAAAG4AAABkCAIAAADoopLKAAABH0lEQVR4nO3QMQ7DIBAAwVP+/2fSIWQcKcWUO9UJY0A7MzMza6211jns9XPDuWfPj5XXxfvYe/PjovvHX5f+8/LX9fvl96d7eJyw588EKSVTSqaUTCmZUjKlZErJlJIpJVNKppRMKZlSMqVkSsmUkiklU0qmlEwpmVIypWRKyZSSKSVTSqaUTCmZUjKlZErJlJIpJVNKppRMKZlSMqVkSsmUkiklU0qmlEwpmVIypWRKyZSSKSVTSqaUTCmZUjKlZErJlJIpJVNKppRMKZlSMqVkSsmUkiklU0qmlEwpmVIypWRKyZSSKSVTSqaUTCmZUjKlZErJlJIpJVNKppRMKZlSMqVkSsmUkiklU0qmlEwpmVIypWRKyZSSKSVTSuYLQYauGbBb3YAAAAAASUVORK5CYII=\n'
b'4IE1fl0YvL'
>> Ouf, merci ! C'est le bon code ! Je fonce vers la porte suivante !

[126/128] Il paraît qu'il y a un mot de passe dans cette image... Peux-tu m'aider ? Vite vite vite !!!

b'iVBORw0KGgoAAAANSUhEUgAAAUoAAABkCAIAAABvmu6gAAABq0lEQVR4nO3TwWrFIBRAwdD//+d0URqKV/uyPsysQlCjhnNdv+77fh5+PC+XN8/zdtacOB+2K8xZy8SPW50r/7OZ0ynmruYX583MTyzT59G2R14GzO++2eTpo6d7265wmrUdtt3bXHmOXKZv35+2/fGiTqd7eYrtz/o7d9nM9h5OJ335L+aw003OHd73/XUBUfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlDlrwhS96QJW/IkjdkyRuy5A1Z8oYseUOWvCFL3pAlb8iSN2TJG7LkDVnyhix5Q5a8IUvekCVvyJI3ZMkbsuQNWfKGLHlD1jdnKuTwKehhEQAAAABJRU5ErkJggg==\n'
b'ZCnb8Mjbylqt0yxR9N6QB0PNubWRf5'
>> Ouf, merci ! C'est le bon code ! Je fonce vers la porte suivante !

[127/128] Il paraît qu'il y a un mot de passe dans cette image... Peux-tu m'aider ? Vite vite vite !!!

b'iVBORw0KGgoAAAANSUhEUgAAARMAAABkCAIAAAAqm0MiAAABe0lEQVR4nO3TSwrCMABAweD976wLUYJpQn3rmYVomzYfeWOM8fwYk/fP7+c85jtyd2W+vhtwmHedel3VfP3mGs5r3t3dreHn+26R62t3b1u3c/nUnW2ut9YB97dz3uZhF+eTPM91+f8ezmF3ILtDu5xunfEwxWMA/1MOFMqBQjlQKAcK5UChHCiUA4VyoFAOFMqBQjlQKAcK5UChHCiUA4VyoFAOFMqBQjlQKAcK5UChHCiUA4VyoFAOFMqBQjlQKAcK5UChHCiUA4VyoFAOFMqBQjlQKAcK5UChHCiUA4VyoFAOFMqBQjlQKAcK5UChHCiUA4VyoFAOFMqBQjlQKAcK5UChHCiUA4VyoFAOFMqBQjlQKAcK5UChHCiUA4VyoFAOFMqBQjlQKAcK5UChHCiUA4VyoFAOFMqBQjlQKAcK5UChHCiUA4VyoFAOFMqBQjlQKAcK5UChHCiUA4VyoFAOFMqBQjlQKAcK5UChHCiUA4VyoFAOFMqB4gV5V5o7kV0L8QAAAABJRU5ErkJggg==\n'
b'ocfDwWf93P8OGfnUzP3ygeBWe'
>> Ouf, merci ! C'est le bon code ! Je fonce vers la porte suivante !

Oh merci merci merci ! Me voilà enfin libre ! Voilà un cadeau pour te remercier :

b'404CTF{W0w_c0d3_128_4_pLUs_4uCuN_s3cr3t_p0uR_t01}\n'
[*] Closed connection to challenge.404ctf.fr port 30566
```

## Python code
Complete solution in [sol.py](./sol.py)

## Flag
404CTF{W0w_c0d3_128_4_pLUs_4uCuN_s3cr3t_p0uR_t01}
