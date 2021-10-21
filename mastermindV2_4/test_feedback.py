import feedback
import partida
import unittest
import random

chute1 = partida.geraSenha(4)
senha1 = partida.geraSenha(4)
chute2 = partida.geraSenha(5)
senha2 = partida.geraSenha(5)
chute3 = partida.geraSenha(6)
senha3 = partida.geraSenha(6)


class testFeedback(unittest.TestCase):
   def test_checaAlgarismos(self):
       testValue1 = feedback.checaAlgarismos(chute1, 4)
       testValue2 = feedback.checaAlgarismos(chute2, 5)
       testValue3 = feedback.checaAlgarismos(chute3, 6)
       mensagemErro = "ERRO - quantidade de algarismos do chute diferente da senha"
       self.assertTrue(testValue1, mensagemErro)
       self.assertTrue(testValue2, mensagemErro)
       self.assertTrue(testValue3, mensagemErro)



   def test_checaJogada(self):
    
        self.assertNotEqual(feedback.checaJogada(senha1, chute1, partida.qtdAlgarismos(senha1)), -1)
        self.assertNotEqual(feedback.checaJogada(senha2, chute2, partida.qtdAlgarismos(senha2)), -1)
        self.assertNotEqual(feedback.checaJogada(senha3, chute3, partida.qtdAlgarismos(senha3)), -1)

        self.assertNotEqual(feedback.checaJogada(senha1, chute1, partida.qtdAlgarismos(senha1)), "")
        self.assertNotEqual(feedback.checaJogada(senha2, chute2, partida.qtdAlgarismos(senha2)), "")
        self.assertNotEqual(feedback.checaJogada(senha3, chute3, partida.qtdAlgarismos(senha3)), "")
        

if __name__ == '__main__':
    unittest.main()


