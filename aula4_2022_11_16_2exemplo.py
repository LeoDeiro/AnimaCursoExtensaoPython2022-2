# Aula 4 - 16/11/2022

#Importar biblioteca:
import sqlite3

#Conectar com o banco de dados:
conexao = sqlite3.connect("dc_universe.db")

#Criar um cursor:
cursor = conexao.cursor()

#Inserir algo no arquivo:
sql = "INSERT INTO pessoas (pessoa_id, nome, nome_civil, tipo) VALUES (12, 'The Flash', 'Barry Allen', 'Herói(na)')"

#Executar o comando SQL:
print(cursor.execute(sql))

#Confirmar o INSERT:
conexao.commit()
conexao.close()