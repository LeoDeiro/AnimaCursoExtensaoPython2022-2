#Criação de Funções

#Função para calcular imposto de 5%
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto

preco = int(input("Insira o valor do produto: "))

imposto = calcular_imposto(preco)

print("O imposto total sobre o produto é de: {} reais".format(imposto))

print(30*("-"))

valores = [43.44, 334.5, 34.56,200,35.35]

for valor in valores:
  print("O imposto do valor {} é {}".format(valor,calcular_imposto(valor)))