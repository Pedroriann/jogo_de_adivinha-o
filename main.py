alvo = 42
try:
    chute = int(input("Digite um numero inteiro entre 0 e 100: "))
    if chute == alvo:
        print("parabens, voce acertou")
    else:
        print("que pena, o numera era " + str(alvo))

except:
    print("numero invalido")