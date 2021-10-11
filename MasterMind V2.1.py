# MasterMind V1

##################################################################################
# ALUNO 1: DAVID WOLFF SALLES DE OLIVEIRA             MATRICULA: 2012428
# ALUNO 2: JOAO GABRIEL CAVALCANTI D NIELSEN          MATRICULA: 1820419
# ALUNO 3: LAIS CORBELLINI FAGUNDES                   MATRICULA: 1720482
# ALUNO 4: MATHEUS AMARAL MENDES FREITAS              MATRICULA: 1712121
##################################################################################


##################################################################################
# IMPORT: Função 'randint' da biblioteca 'random'
# OBJETIVO: Função que permite gerar um número aleatorio a partir de um intervalo
#           (a,b) passado como parâmetro com, a e b inclusivos
##################################################################################
from random import randint


##################################################################################
# NOME: geraSenha
# OBJETIVO: Função que gera uma senha de forma aleatoria, utilizando a biblioteca  
#           random, com a quantidade de algarismos recebidos como parâmetro
##################################################################################
def geraSenha(numAlgarismos):
    return str(randint(10**(numAlgarismos-1),10**numAlgarismos-1))


##################################################################################
# NOME: qtdAlgarismos
# OBJETIVO: Função que recebe uma senha e retorna a quantidade de algarismo do
#           número, usando a funcao "len"
##################################################################################
def qtdAlgarismos(senha):
    return len(senha)


##################################################################################
# NOME: checaAlgarismos
# OBJETIVO: Função que recebe uma senha a quantidade de algarismos que ela deve 
#           ter e, retorna: True, se a senha tem a quantidade exata de digitos
#                           False, se ela tem uma quatidade incorreta de digitos   
##################################################################################
def checaAlgarismos(senhaChute,numAlgarismos):
    return qtdAlgarismos(senhaChute) == numAlgarismos


##################################################################################
# NOME: jogadaUsuario
# OBJETIVO: Função que recebe a quantidade de algarismos da senha e pede para o
#           usuário informar via teclado os digitos do seu chute
##################################################################################
def jogadaUsuario(numAlgarismos):
    return input("\nEntre com os %d digitos da senha: "%numAlgarismos)


##################################################################################
# NOME: checaJogada
# OBJETIVO: Função que recebe a senha chute do usuario e a verifica: exibindo uma
#           mensagem de erro ou retornando feedback da senha (acertos e erros)
##################################################################################
def checaJogada(senha,senhaChute,numAlgarismos):

    if not checaAlgarismos(senhaChute,numAlgarismos):
        print("Quantidade de digitos incorreto!")
        return -1
        
    feedbackChute = ""
    for (pos,digito) in enumerate(senhaChute):

        if digito == senha[pos]:
            feedbackChute += digito
        elif digito in senha:
            feedbackChute += "?"
        else:
            feedbackChute += "X"

    return feedbackChute


##################################################################################
# NOME: oJogo
# OBJETIVO: Função principal que roda o jogo como um todo
##################################################################################
def oJogo(jogadas,numAlgarismos):

    senha = geraSenha(numAlgarismos)
    print(senha)

    qtdJogadas = 1
    while (qtdJogadas <= jogadas):

        senhaChute = jogadaUsuario(numAlgarismos)
        feedbackJogada = checaJogada(senha,senhaChute,numAlgarismos)

        while feedbackJogada == -1:
            senhaChute = jogadaUsuario(numAlgarismos)
            feedbackJogada = checaJogada(senha,senhaChute,numAlgarismos)
            
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


##################################################################################
# NOME: main
# OBJETIVO: Função que inicializa o jogo
##################################################################################
def main():

    print("* Bem vindo ao Jogo MasterMind de progModular *")

    nivel = qualNivel()

    print("\n* Ok! Vamos começar! *")
    oJogo(nivel[0],nivel[1])
    print("\n* Fim! Obrigado por jogar MasterMind! *")
    
    return


main()
