# Stego / PNG: un logo obèse [1/4]

## Challenge
L'heure est grave. Hallebarde ne se cache plus et échange des messages en toute liberté. Un tel manque de précautions de leur part est alarmant, et même presque suspect. Un logo a été utilisé dans l'un de leurs courriels et d'après de premières analyses, il pourrait avoir été employé pour ouvrir un canal de stéganographie. Pourriez-vous tirer cela au clair ?

## Inputs
- PNG file: [steg.png](./steg.png)

## Solution
Let's `binwalk`, to find a hidden `stage2.png`:
```console
$ binwalk steg.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1103 x 319, 8-bit/color RGBA, non-interlaced
30474         0x770A          Zip archive data, at least v2.0 to extract, compressed size: 495679, uncompressed size: 497701, name: out/stage2.png
526309        0x807E5         End of Zip archive, footer length: 22
```

Let's extract it using option `-e`:
```console
$ binwalk -e steg.png

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1103 x 319, 8-bit/color RGBA, non-interlaced
30474         0x770A          Zip archive data, at least v2.0 to extract, compressed size: 495679, uncompressed size: 497701, name: out/stage2.png
526309        0x807E5         End of Zip archive, footer length: 22

$ ll
total 524
-rw-r--r-- 1 thesee thesee 526331 May 17 23:22 steg.png
drwxr-xr-x 3 thesee thesee   4096 May 18 00:01 _steg.png.extracted

$ cd _steg.png.extracted
$ ll
total 492
-rw-r--r-- 1 thesee thesee 495857 May 18 00:01 770A.zip
drwxr-xr-x 2 thesee thesee   4096 May 18 00:01 out
$ ll out
total 488
-rw-r--r-- 1 thesee thesee 497701 May 11 23:40 stage2.png
```

![stage2.png](./stage2.png)

## Flag
404CTF{0b3z3_f1l3_h4z_zup3r_spy_s3cr37}
