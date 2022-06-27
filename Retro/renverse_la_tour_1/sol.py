#!/usr/bin/python3

ENC_PWD = "¡P6¨sÉU1T0d¸VÊvçu©6RÈx¨4xFw5"

def r_tour1(password):
    return password[::-1]

def r_tour2(password):
    return password[0::2]

def r_tour3(password):
    mdp = ['l', 'x', 'i', 'b', 'i', 'i', 'q', 'u', 'd', 'v', 'a', 'v', 'b', 'n', 'l', 'v', 'v', 'l', 'g', 'z', 'q', 'g', 'i', 'u', 'd', 'u', 'd', 'j', 'o', 'r', 'y', 'r', 'u', 'a']
    for i in range(len(password)):
        mdp[i] = ord(password[len(password) - i -1 ]) - i % 4
        mdp[len(password) - i -1 ] = ord(password[i]) - i % 4
    return mdp

mdp_ = r_tour1(r_tour2(r_tour3(ENC_PWD)))
print(''.join([chr(x) for x in mdp_]))

# P4sS1R0bUst3Qu3C4
