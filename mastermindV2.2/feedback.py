import random
import partida 

##################################################################################
# NOME: checaAlgarismos
# OBJETIVO: Função que recebe uma senha a quantidade de algarismos que ela deve 
#           ter e, retorna: True, se a senha tem a quantidade exata de digitos
#                           False, se ela tem uma quatidade incorreta de digitos   
##################################################################################
def checaAlgarismos(senhaChute,numAlgarismos):
    return partida.qtdAlgarismos(senhaChute) == numAlgarismos

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