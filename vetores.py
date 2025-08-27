#Fazer um programa para ler um número inteiro positivo N(máximo = 10),depois ler N números quaisquer e armazená-los em um vetor.
#Em seguida,mostrar na tela todos elementos do vetor.

N: int
N = int(input("Quantos numeros voce vai digitar? "))
vet: [float] = [0 for x in range(N)]

for i in range(0, N):
    vet[i] = float(input("Digite um numero: "))

print()
print("NUMEROS DIGITADOS:")
for i in range(0, N):
        print(f"{vet[i]:.1f}")