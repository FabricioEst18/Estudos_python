#Estrutura condicional simples
x = 10

print("Bom dia!")
if x < 0:
    print("Boa tarde!")
print("Boa noite!")

#Estrutura condicional composta
hora : int

hora = int(input("Digite uma hora do dia: "))

if hora > 12: 
    print("Bom dia!")
else:
    print("Boa noite")

#Encadeamento
hora2 : int

hora2 = int(input("Digite uma hora do dia: "))
if hora2 > 12:
    print("Bom dia!")
elif hora2 > 18:
    print("Boa tarde!")
else:
    print("Boa noite!")