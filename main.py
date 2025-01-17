alvo = 42
quantidade_tentativas = 5
jogador_acertou = False
while quantidade_tentativas > 0 and not jogador_acertou :
    try:
        chute = int(input("Digite um numero inteiro entre 0 e 100: "))
        if chute == alvo:
            print("parabens, voce acertou")
            jogador_acertou = True
        elif chute > alvo:
            print("errou o numero é menor")
            quantidade_tentativas -= 1
        else: 
             print("errou o numero é maior")
             quantidade_tentativas += 1
            
    except:
        print("numero invalido")
if not jogador_acertou:
     print("que pena, o numera era " + str(alvo))