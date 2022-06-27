# Coding / Compression

## Challenge
Après une intervention, nous avons récupéré un fichier ultra-secret; le Fichier Légitime Arbitrairement Gros. Abrégé en "flag", nous pensons qu'il contient des secrets de Hallebarde. Hélàs, comme ce fichier est supposément très lourd, il a été compressé un très grand nombre de fois de plusieurs manières différentes et nous n'arrivons pas à en récupérer le contenu. Pouvez-vous y aider ?

## Inputs
- [flag2500.tar.gz](./flag2500.tar.gz)

## Solution
Decompressing `flag2500.tar.gz` results in a new compressed file, so we understand we have a regression of presumably 2500 files to decompress one after another, possibly with different compressed formats. So we have to automate it. Here is my code using bash script [sol.sh](./sol.sh):
```bash
for i in {2500..1..-1}
do
    echo $i
    if [[ -e flag$i.tar.gz ]]; then
        gunzip flag$i.tar.gz
        tar xvf flag$i.tar
    elif [[ -e flag$i.tar ]]; then
        tar xvf flag$i.tar
    elif [[ -e flag$i.tar.xz ]]; then
        tar xvf flag$i.tar.xz
    elif [[ -e flag$i.tar.bz2 ]]; then
        bzip2 -d flag$i.tar.bz2
        tar xvf flag$i.tar
    else
        exit
    fi
done
```

Here is the output of the execution:
```console
$ bash sol.sh
flag2499.tar.gz
flag2498.tar
flag2497.tar.xz
flag2496.tar.xz
flag2495.tar
flag2494.tar
flag2493.tar.gz
flag2492.tar
flag2491.tar.gz
(...)
flag7.tar.gz
flag6.tar
flag5.tar.gz
flag4.tar.gz
flag3.tar.bz2
flag2.tar.bz2
flag1.tar.bz2
flag.txt

$ cat flag.txt
404CTF{C0mPr3Ssi0n_m4X1m4L3_m41S_p4S_3ff1C4c3}
```

## Bash script
Complete solution in [sol.sh](./sol.sh)

## Flag
404CTF{C0mPr3Ssi0n_m4X1m4L3_m41S_p4S_3ff1C4c3}
