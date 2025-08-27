# #Comando de entrada de dados:
# #O comando input() é para ler dados do tipo TEXTO→str
# input("Mensagem")


# #Se precisar ler uma variável do tipo int,faça:
# x = int(input("Digite um número: "))

# #Se precisar ler uma variável do tipo float,faça:
# y =  float(input("Digite um número: "))

salario1 : float; salario2 : float
nome1 : str; nome2 : str
idade : int
sexo : str

nome1 = input("Nome da primeira pessoa: ")
salario1 = float(input("Salário da primeira pessoa: "))

nome2 = input("Nome da primeira pessoa: ")
salario2 = float(input("Salário da segunda pessoa: "))

idade = int(input("Digite uma idade: "))
sexo = input("Digite um sexo (F/M): ")

print(f"Nome: {nome1}")
print(f"Salário: {salario1:.2f}")
print(f"Nome: {nome2}")
print(f"Salário: {salario2:.2f}")
print(f"Idade: {idade}")
print(f"Sexo: {sexo}")

