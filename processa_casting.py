a : int 
b: int 
resultado: int

a = 5
b = 2
resultado = a / b #O resultado é 2.5,porém colocamos o resultado para vir com int

#O resultado,mesmo com a variável sendo int vai 2.5,pois ele dá prioridade a inferência da divisão acima que é float.Para ser inteiro devemos usar o operador //
print(resultado)


x : float 
y : int

x = 5.2
y = x #Irá imprimir o valor de y como 5.2,se quisermos que o valor seja realmente int devemos fazer y = int(x)
print(y)