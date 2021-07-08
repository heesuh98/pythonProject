n_pivo = int(input("pivo:"))
l_pibo = [1,1]

def pivo(n):
    while len(l_pivo) <n:
        l_pivo.append(l_pivo[-1]+l_pivo[-2])
