userinput = [ord(e) for e in input('Password:')]
key = 'd1j#H(&Ja1_2 61fG&'

def code(l):
    match l:
        case [el, *rest]:
            return [5*el ^ ord(key[len(rest) % len(key)])] + code(rest)
        case []:
            return []

if code(userinput) == [292, 194, 347, 382, 453, 276, 577, 434, 183, 295, 318, 196, 482, 325, 412, 502, 396, 402, 328, 194, 473, 490, 299, 503, 386, 215, 263, 211, 318, 206, 533]:
    print('Bravo!')
else:
    print('Dommage...')
