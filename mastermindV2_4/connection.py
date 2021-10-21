import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost', 
                                         database ='partidas', 
                                         user='root', 
                                         password='banzaiPipeleme_0')
    
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Conectado ao mySql Server versao ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database()")
        record = cursor.fetchone()
        print("Conectado ao banco de dados: ", record)
except Error as e:
    print("Erro de conexao", e)
finally:
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Conexao Encerrada")