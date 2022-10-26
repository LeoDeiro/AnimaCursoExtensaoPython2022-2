# Aula 2

# input(): (o usuário digita)

nome = input("Digite o seu nome: ")
print("Seu nome é "+nome)

#colocar o int antes para declarar números
idade = int(input("\nDigite sua idade: "))
print("Sua idade é {}".format(idade))

dobro = idade * 2

print("O dobro da sua idade é {}".format(dobro))

print(30*"-")
numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

soma = numero1 + numero2
multi = numero1 * numero2

print("\nA soma destes números é: {}".format(soma))
print("A multiplicação destes números é: {}".format(multi))