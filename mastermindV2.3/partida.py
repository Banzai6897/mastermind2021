
from random import randint
import jogada 
import feedback

##################################################################################
# NOME: qtdAlgarismos
# OBJETIVO: Função que recebe uma senha e retorna a quantidade de algarismo do
#           número, usando a funcao "len"
##################################################################################
def qtdAlgarismos(senha):
    return len(senha)
    
##################################################################################
# NOME: geraSenha
# OBJETIVO: Função que gera uma senha de forma aleatoria, utilizando a biblioteca  
#           random, com a quantidade de algarismos recebidos como parâmetro
##################################################################################
def geraSenha(numAlgarismos):
    return str(randint(10**(numAlgarismos-1),10**numAlgarismos-1))
##################################################################################
# NOME: oJogo
# OBJETIVO: Função principal que roda o jogo como um todo
##################################################################################
def oJogo(jogadas,numAlgarismos):

    senha = geraSenha(numAlgarismos)
    print(senha)

    qtdJogadas = 1
    while (qtdJogadas <= jogadas):

        senhaChute = jogada.jogadaUsuario(numAlgarismos)
        feedbackJogada = feedback.checaJogada(senha,senhaChute,numAlgarismos)

        while feedbackJogada == -1:
            senhaChute = jogada.jogadaUsuario(numAlgarismos)
            feedbackJogada = feedback.checaJogada(senha,senhaChute,numAlgarismos)
            
        if feedbackJogada == senha:
            print("Parabéns, você venceu!")
            return

        print("->",feedbackJogada)
        print("-> Restam %d jogadas!"%(jogadas-qtdJogadas))

        qtdJogadas += 1

    print("Game Over! Você excedeu o número de tentativas!")
    return
##################################################################################
# NOME: nivelJogo
# OBJETIVO: Função que retorna, em forma de tupla, as infos de cada nível do jogo
#           - Nivel 1:  8 jogadas e senha de 4 digitos
#           - Nivel 2: 10 jogadas e senha de 5 digitos
#           - Nivel 3: 12 jogadas e senha de 6 digitos
##################################################################################
def nivelJogo(nivel):
    
    if nivel == 1:
        return (8,4)
    elif nivel == 2:
        return (10,5)
    elif nivel == 3:
        return (12,6)
    else:
        return -1
##################################################################################
# NOME: qualNivel
# OBJETIVO: Função que pergunta ao usuario em qual nivel deseja jogar
##################################################################################
def qualNivel():

    print("\nInforme o nível que deseja jogar (1,2 ou 3)")
    print("- (1) Fácil")
    print("- (2) Médio")
    print("- (3) Difícil")
    return nivelJogo(int(input("- Nível desejado: ")))
