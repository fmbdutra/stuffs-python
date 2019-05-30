from random import randint

class RF:
    def __init__(self):
        pass

    def set_rg(self):
        numeros = ''
        for n in range(8):
            numeros += str(randint(0, 9))

        soma_produtos = 0
        for i, n in enumerate(numeros):
            soma_produtos += int(n) * (i+2)

        if soma_produtos % 11 > 2:
            numeros += str(11 - (soma_produtos % 11))
        else:
            numeros += '0'

        return numeros


    def set_numero(self):
        numero = '519'
        numero += str(randint(1,9))
        for n in range(7):
            numero += str(randint(0,9))
        return numero