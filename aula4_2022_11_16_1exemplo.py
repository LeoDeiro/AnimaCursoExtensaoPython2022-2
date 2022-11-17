# Aula 4 - 16/11/2022

#Importar biblioteca:
import sqlite3

#Conectar com o banco de dados:
conexao = sqlite3.connect("dc_universe.db")

#Criar um cursor:
cursor = conexao.cursor()

#Comando SQL do banco:
sql = "SELECT pessoa_id, nome, nome_civil, tipo FROM pessoas"

#Executar o comando SQL no SQLlite:
cursor.execute(sql)

#Exibir a consulta:
pessoas = cursor.fetchall()
for pessoa in pessoas:
  print(pessoa)

print(45*("-"))

for pessoa in pessoas:
  print("Nome: {} ({})".format(pessoa[1],pessoa[3]))