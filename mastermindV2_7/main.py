
from random import randint
import partida
import mysql.connector
import connection
from mysql.connector import Error

                                     
##################################################################################
# NOME: main
# OBJETIVO: Função que inicializa o jogo
##################################################################################
def main():

    user = partida.criaUserName()

    nivel = partida.qualNivel()

    print("\n* Ok", user, "Vamos começar! *")
    qtdJogadas, resultado = partida.oJogo(nivel[0],nivel[1]) 
    
    print("\n* Fim! Obrigado por jogar MasterMind! *\n")

    connection.registroPartidas(nivel, user, qtdJogadas, resultado)
        
    return 


if __name__ == "__main__":
    main()
