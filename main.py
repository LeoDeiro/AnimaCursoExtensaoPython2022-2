# Aula 2

# input(): (o usuário digita)

nome = input("Digite o seu nome: ")
print("Seu nome é "+nome)

#colocar o int antes para declarar números
idade = int(input("\nDigite sua idade: "))
print("Sua idade é {}".format(idade))

genero = input("Informe seu gênero M para masculino e F para feminino: ")

'''
dobro = idade * 2
print("O dobro da sua idade é {}".format(dobro))
'''
#if condicional

if (idade >= 18):
  print("Você é maior de idade.")
  if(genero == "M"):
    print("Você deverá se alistar!")
else:
  print("Você é menor de idade.")
print(30*"-")


