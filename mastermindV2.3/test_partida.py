import partida
import unittest



class testPartida(unittest.TestCase):
    
    def test_geraSenha(self):
        senha1 = partida.geraSenha(4) 
        senha2 = partida.geraSenha(5)
        senha3 = partida.geraSenha(6)
        self.assertEqual(partida.qtdAlgarismos(senha1), 4)
        self.assertEqual(partida.qtdAlgarismos(senha2), 5)
        self.assertEqual(partida.qtdAlgarismos(senha3), 6)
        
    def test_nivelJogo(self):

        self.assertEqual(partida.nivelJogo(1), (8,4))
        self.assertEqual(partida.nivelJogo(2), (10,5))
        self.assertEqual(partida.nivelJogo(3), (12,6))
        self.assertEqual(partida.nivelJogo(4), -1)
        self.assertEqual(partida.nivelJogo(0), -1)

        
        



if __name__ == '__main__':
    unittest.main()
