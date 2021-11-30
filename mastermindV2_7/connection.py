import partida
import main
import mysql.connector
from mysql.connector import Error
from xml.etree import *
from xml.etree.ElementTree import *


def criaDBmySQL():
    try:
        connection = mysql.connector.connect(host='localhost', 
                                             user='root', 
                                             password='banzaiPipeleme_0')
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS partidasMastermind2_6;")
        connection.commit()

    except Error as e:
        print("Erro de conexao", e)
        return 0

    finally:
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print("Base de dados partidasMastermind2_6 criada ou existente em localhost. ")

    return 1


def registroPartidas(nivel, user, qtdJogadas, resultado):
    dbExiste = criaDBmySQL()
    if dbExiste == 1:
        record = (user, qtdJogadas,resultado)
        try:
            connection = mysql.connector.connect(host='localhost', 
                                                 user='root', 
                                                 database ='partidasMastermind2_6',
                                                 password='banzaiPipeleme_0',
                                                 )

            cursor = connection.cursor()
            
            cursor.execute("CREATE TABLE IF NOT EXISTS nivel1 (user VARCHAR(8), tentativas INT(1), resultado CHAR(6), PRIMARY KEY(user));")
            cursor.execute("CREATE TABLE IF NOT EXISTS nivel2 (user VARCHAR(8), tentativas INT(2), resultado CHAR(6), PRIMARY KEY(user));")
            cursor.execute("CREATE TABLE IF NOT EXISTS nivel3 (user VARCHAR(8), tentativas INT(2), resultado CHAR(6), PRIMARY KEY(user));")
            
            if nivel==(8,4):
                sql = ("""INSERT INTO nivel1 (user, tentativas, resultado) VALUES (%s, %s, %s);""")
                cursor.execute(sql, record)
            elif nivel==(10,5):
                sql = ("""INSERT INTO nivel2 (user, tentativas, resultado) VALUES (%s, %s, %s);""")
                cursor.execute(sql, record)
            elif nivel==(12,6):
                sql = ("""INSERT INTO nivel3 (user, tentativas, resultado) VALUES (%s, %s, %s);""")
                cursor.execute(sql, record)
            connection.commit()
            
            if nivel==(8,4):
                cursor.execute("SELECT * FROM nivel1")
                result = cursor.fetchall()
                nivelPartida = str(1)
                print("\n\tRANKING DOS USUARIOS QUE JOGARAM NESTA MAQUINA NO NIVEL", nivelPartida,  ":\n")
                print("\n\tUSUARIO - NUMERO DE  TENTATIVAS - RESULTADO FINAL\n")
            elif nivel ==(10,5):
                cursor.execute("SELECT * FROM nivel2")
                result = cursor.fetchall()
                nivelPartida = str(2)
                print("\n\tRANKING DOS USUARIOS QUE JOGARAM NESTA MAQUINA NO NIVEL", nivelPartida, ":\n")
                print("\n\tUSUARIO - NUMERO DE  TENTATIVAS - RESULTADO FINAL\n")
            elif nivel ==(12,6):
                cursor.execute("SELECT * FROM nivel3")
                result = cursor.fetchall()
                nivelPartida = str(3)
                print("\n\tRANKING DOS USUARIOS QUE JOGARAM NESTA MAQUINA NO NIVEL", nivelPartida, ":\n")
                print("\n\tUSUARIO - NUMERO DE  TENTATIVAS - RESULTADO FINAL\n")
            
            for row in result:
                print("\t", row, "\n")

            cursor.close()

        except Error as e:
            print("Erro de conexao", e)

        finally:
            if(connection.is_connected()):
                cursor.close()
                connection.close()
                print("Conexao Encerrada")
    elif dbExiste == 0:
        print("Erro na criacao da base de dados.")

    cria_xml(result, nivelPartida)
    return

def cria_xml(lista, nivel):
    rootEl = Element("Mastermind - Relacao de Partidas no nivel " + nivel)
    
    for item in range(len(lista)):
        partida = SubElement(rootEl, "partida -> Usuario - Tentativas - Resultado")
        partida.text = str(lista[item])
    tree = ElementTree(rootEl)
    tree.write("partidas.xml", xml_declaration=True) 