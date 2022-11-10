#Aula 3 09/11/2001

#criar uma "lista" (array)
frutas = ["Morango","Laranja","Manga"]

print(frutas[2])

#len (lenght) = tamanho
print(len(frutas))

#adicionar algo no fim da lista
frutas.append("Abacaxi")
print(len(frutas))

print(frutas)
print(30*("-"))
print("Exemplo com o WHILE:\n")
#print com while
i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

print(30*("-"))
print("Exemplo com o FOR:\n")
#print com for
for lista in frutas:
 print(lista)

print(30*("-"))
fruta = input("Insira uma fruta na lista: ")
frutas.append(fruta)

for lista in frutas:
 print(lista)