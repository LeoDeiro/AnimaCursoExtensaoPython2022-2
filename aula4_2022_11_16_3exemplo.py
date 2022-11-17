# Aula 4 - 16/11/2022

#Importar biblioteca:
import sqlite3

#Função conectar():
def conectar():
  #Conectar com o banco de dados:
  conexao = sqlite3.connect("dc_universe.db")
  #Criar um cursor:
  cursor = conexao.cursor()

  return conexao, cursor
