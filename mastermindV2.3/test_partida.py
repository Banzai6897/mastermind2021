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
        

    

        
        



if __name__ == '__main__':
    unittest.main()