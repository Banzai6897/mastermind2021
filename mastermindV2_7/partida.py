
from random import randint
import jogada 
import feedback

def criaUserName():
    user = str(input("Bem vind@ ao jogo\n\n\tM\tA\tS\tT\tE\tR\tM\tI\tN\tD\n\n\ninsira um nome de usuário com até 8 caracteres para iniciar o jogo."))
    return user
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
    dig01 = randint(1,7)
    dig02 = randint(1,7)
    dig03 = randint(1,7)
    dig04 = randint(1,7)
    dig05 = randint(1,7)
    dig06 = randint(1,7)
    strDig01 = str(dig01)
    strDig02 = str(dig02)
    strDig03 = str(dig03)
    strDig04 = str(dig04)
    strDig05 = str(dig05)
    strDig06 = str(dig06)

    if numAlgarismos == 4:
        senha = strDig02 + strDig01 + strDig03 + strDig04
    elif numAlgarismos == 5:
        senha = strDig01 + strDig04 + strDig03 + strDig05  + strDig02
    elif numAlgarismos == 6:
        senha = strDig01 + strDig02 + strDig04 + strDig06  + strDig05 + strDig03
    
    return senha
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
            resultado = "Ganhou"
            return qtdJogadas, resultado 

        print("->",feedbackJogada)
        print("-> Restam %d jogadas!"%(jogadas-qtdJogadas))

        qtdJogadas += 1

    
    print("Game Over! Você excedeu o número de tentativas!")
    resultado = "Perdeu"

    return qtdJogadas - 1, resultado
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
