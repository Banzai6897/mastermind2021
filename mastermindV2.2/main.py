
from random import randint

import partida

##################################################################################
# NOME: main
# OBJETIVO: Função que inicializa o jogo
##################################################################################
def main():

    run = True

    print("* Bem vindo ao Jogo MasterMind de progModular *")

    nivel = partida.qualNivel()

    print("\n* Ok! Vamos começar! *")
    partida.oJogo(nivel[0],nivel[1])
    print("\n* Fim! Obrigado por jogar MasterMind! *")
    
    return

if __name__ == "__main__":
    main()
