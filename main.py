def adivinhe_o_numero():
    print("Você escolheu Adivinhe o Número!")
    import random
    numero = random.randint(1, 10)
    while True:
        palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))
        if palpite == numero:
            print("Parabéns! Você acertou!")
            break
        elif palpite < numero:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")
