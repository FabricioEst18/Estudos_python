#int → número inteiro 
#float → números reais e frações
#str → um único caractere(parecido com o char)
#str → texto 
#boolean → valor lógico(true/false)


#Python é uma linguagem INTERPRETADA,com base no valor atribuído a variável ele sabe de qual tipo ela é,
# mas como uma forma de “DICA” podemos passar o tipo da variável para o interpretador


#A declaração dos tipos de cada variável no python é opcional!
idade: int
salario: float
altura: float
genero: str
nome: str

idade = 20
salario = 5800.5
altura = 1.63
genero = "F"
nome = "Maria Silva"

#Usando o f"" podemos INTERPOLAR valores diretamente dentro de uma string
print(f"IDADE = {idade}")
print(f"SALARIO = {salario:.2f}")
print(f"ALTURA = {altura:.2f}")
print(f"GENERO = {genero}")
print(f"NOME = {nome}")
