#Por padrão,o interpretador do python irá imprimir a saída dos dados um embaixo do outro:
print("Bom dia!")
print("Boa noite!")

#Se quisermos imprimir um na frente do outro devemos fazer o seguinte:
print("Bom dia!", end="") #Usando o "end=" ele não irá quebrar linha
print("Boa noite!")

#Saída de dados com variáveis pré-declaradas
x : int, y : int

x = 10
y = 20

print(x)
print(y)

#Impressão de uma variável float,formatando ela:
x : float
x = 2.3456
print("{:.2f}".format(x))#{:.2f} → Imprime duas casas depois da vírgula


#Imprimir dados com interpolação:
idade : int
salario : float
nome : str
sexo : str

idade = 32 
salario = 4560.9
nome = "Maria Silva"
sexo = "F"

print(f"A funcionaria {nome}, sexo {sexo}, ganha{salario:.2f} e tem {idade} anos")

#Usando os placeholder's de formatação,não muito usual mas dá pra fazer
print("A funcionaria {:s}, sexo {:s}, ganha {:.2f}e tem {:d} anos".format(nome, sexo, salario,idade))
