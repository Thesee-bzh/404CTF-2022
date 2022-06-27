#  Forensics / Ping Pong

## Challenge
Nous avons repéré une communication bizarre provenant des serveurs de Hallebarde. On soupçonne qu'ils en aient profité pour s'échanger des informations vitales. Pouvez-vous investiguer ?

## Inputs
- PCAP file: [ping.pcapng](./ping.pcapng)

## Solution
The PCAP file shows a lot of `ICMP` ping requests, with data included. The data is responded back in the `ICMP` ping response, so we can focus on the `ICMP` requests alone.

Here is the first packet:
```
Frame 1: 94 bytes on wire (752 bits), 94 bytes captured (752 bits) on interface enp0s8, id 0
Ethernet II, Src: PcsCompu_cb:f6:73 (08:00:27:cb:f6:73), Dst: PcsCompu_75:4f:c7 (08:00:27:75:4f:c7)
Internet Protocol Version 4, Src: 10.1.0.10, Dst: 10.1.0.1
Internet Control Message Protocol
    Type: 8 (Echo (ping) request)
    Code: 0
    Checksum: 0x8253 [correct]
    [Checksum Status: Good]
    Identifier (BE): 21663 (0x549f)
    Identifier (LE): 40788 (0x9f54)
    Sequence Number (BE): 256 (0x0100)
    Sequence Number (LE): 1 (0x0001)
    Data (52 bytes)

0000  50 54 58 41 46 34 53 31 33 32 4f 4d 4d 53 45 39   PTXAF4S132OMMSE9
0010  4e 50 30 54 4a 35 56 49 33 42 4a 49 58 54 33 57   NP0TJ5VI3BJIXT3W
0020  4f 31 57 4c 42 41 35 4f 35 4f 39 33 41 38 51 47   O1WLBA5O5O93A8QG
0030  38 42 49 59                                       8BIY
        Data: 505458414634533133324f4d4d5345394e5030544a35564933424a49585433574f31574c…
        [Length: 52]
```

I could not make any sense of the data itself, nor individually, nor after concatenation of all data from all ICMP ping requests.

A tip was given to look at `around` the data itself, which led me to look at the length of the data. Let's extract the IP packet lengths with `tshark`.

```console
$ tshark -r ping.pcapng -O icmp -Y 'ip.src==10.1.0.10 and icmp' -Tfields -e ip.len > ip_len.txt
$ cat ip_len.txt
80
76
80
95
112
98
151
113
138
123
140
77
138
131
123
140
76
138
131
123
140
80
143
123
143
133
123
77
138
138
76
127
79
138
144
153
```

IP header is 20 bytes and ICMP header is 8 bytes, so substract 28 bytes to the total IP packet length to get the length of the ICMP data. Let's script that:

```python
data = ''
with open("ip_len.txt", "r") as f:
    for line in f:
        length = int(line.strip())
        if length:
            data += chr(length - 28)
print(data)
```

```console
$ python3 sol.py
404CTF{Un_p1ng_p0ng_p4s_si_1nn0c3nt}
```

## Python code
Complete solution in [sol.py](./sol.py)

## Flag
404CTF{Un_p1ng_p0ng_p4s_si_1nn0c3nt}
