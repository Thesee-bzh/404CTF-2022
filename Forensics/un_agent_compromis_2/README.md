#  Forensics / Un agent compromis [2/3]

## Challenge
Maintenant, nous avons besoin de savoir quels fichiers il a exfiltré.

Format du flag : 404CTF{fichier1,fichier2,fichier3,...} Le nom des fichiers doit être mis par ordre alphabétique.

## Inputs
- PCAP file: [capture-reseau.pcapng](../un_agent_compromis_1/capture-reseau.pcapng)

## Solution
In python file `exfiltration.py`, we see following `DNS queries` for each exfiltrated file:
- "never-gonna-give-you-up.hallebarde.404ctf.fr"
- binascii.hexlify(filename.encode()).decode() + ".hallebarde.404ctf.fr"
- "626567696E.hallebarde.404ctf.fr"
- hostname + ".hallebarde.404ctf.fr", in chunks of 32 bytes
- "656E64.hallebarde.404ctf.fr"

Let's extract the `DNS names` like `*.hallebarde.*` from the DNS queries in the PCAP file:
```console
$ tshark -r capture-reseau.pcapng  -O dns -Y 'ip.src==192.168.122.55' -T fields -e dns.qry.name | grep hallebarde > dns_names.txt
```

Here are the first outputs:
```console
$ cat dns_names.txt
hallebarde.404ctf.fr
hallebarde.404ctf.fr
never-gonna-give-you-up.hallebarde.404ctf.fr
666c61672e747874.hallebarde.404ctf.fr
626567696E.hallebarde.404ctf.fr
3430344354467b706173206c6520666c.hallebarde.404ctf.fr
61672c20646f6d6d616765203a707d0a.hallebarde.404ctf.fr
656E64.hallebarde.404ctf.fr
never-gonna-give-you-up.hallebarde.404ctf.fr
68616c6c6562617264652e706e67.hallebarde.404ctf.fr
626567696E.hallebarde.404ctf.fr
89504e470d0a1a0a0000000d49484452.hallebarde.404ctf.fr
0000044f0000013f0806000000b7b8ed.hallebarde.404ctf.fr
710000200049444154789cec9d07d41e.hallebarde.404ctf.fr
45d5c7ff2f09a197d04327447a0f5544.hallebarde.404ctf.fr
10225da94144a409114414110c882245.hallebarde.404ctf.fr
20a808a89420284504838234e9a022d2.hallebarde.404ctf.fr
42119022841ae9090142204092efccc7.hallebarde.404ctf.fr
7de461d9dd67cb943bbbffdf39f77c7e.hallebarde.404ctf.fr
e4797767efccecccdeb9058410420821.hallebarde.404ctf.fr
(...)
```

The DNS requests corresponding to the exfiltrated file names appear right after the one for `never-gonna-give-you-up.hallebarde.404ctf.fr`.
```console
$ grep -A1 never dns_names.txt
never-gonna-give-you-up.hallebarde.404ctf.fr
666c61672e747874.hallebarde.404ctf.fr
--
never-gonna-give-you-up.hallebarde.404ctf.fr
68616c6c6562617264652e706e67.hallebarde.404ctf.fr
--
never-gonna-give-you-up.hallebarde.404ctf.fr
73757065722d7365637265742e706466.hallebarde.404ctf.fr
--
never-gonna-give-you-up.hallebarde.404ctf.fr
657866696c74726174696f6e2e7079.hallebarde.404ctf.fr

```

So the file names are:
- 666c61672e747874
- 68616c6c6562617264652e706e67
- 73757065722d7365637265742e706466
- 657866696c74726174696f6e2e7079

We just have to `unhexlify` them:
```python
import binascii
for file in ['666c61672e747874', '68616c6c6562617264652e706e67', '73757065722d7365637265742e706466', '657866696c74726174696f6e2e7079']:
    print(binascii.unhexlify(file).decode())
```

Here the are:
```console
flag.txt
hallebarde.png
super-secret.pdf
exfiltration.py
```

The flag is 404CTF{file1,file,file3,...} with files in alphabetic order.

## Flag
404CTF{exfiltration.py,flag.txt,hallebarde.png,super-secret.pdf}
