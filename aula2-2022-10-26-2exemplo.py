# Pedir o nome do aluno e a nota

nome = input("Insira seu nome: ")
nota = float(input("Digite sua nota: "))

if(nota == 10):
  print("Parabéns {}!".format(nome))
elif(nota < 10 and nota >= 7):
  print("Você passou!")
elif(nota == 6):
  print("Você passou na média.")
elif(nota < 6 and nota >= 0):
  print("Você reprovou. :(")
elif(nota > 10 or nota < 0):
  print("Insira um valor entre 0 e 10.")
  