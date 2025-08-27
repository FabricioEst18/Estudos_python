#Fazer um programa que lê um valor inteiro N e depois N números inteiros. Ao final,mostra a soma dos N números lidos
x : int
soma : int

N = int(input("Quantos numeros serao digitados? "))

soma = 0
for i in range(0, N):
    x = int(input("Digite um numero: "))
    soma = soma + x

print("SOMA = ", soma)