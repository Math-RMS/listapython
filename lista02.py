#Criando lista
minha_lista = [1,2,3,4,5]
# Usando um loop for para pecorrer a lista e imprimir cada elemento 
for i in range(len(minha_lista)):
    print("O elemento", i+1, "da lista é:", minha_lista[i])
    
#Criando uma lista de números
numeros = [1,2,3,4,5]
# Usando um loop for para pecorrer a lista e imprimir cada elemento 
for numero in numeros:
    print(numero, " - Com for")
    
# Usando um loop for para pecorrer a lista e imprimir cada elemento 
i = 0
while i < len(numeros):
    print(numeros[i], " - Com while")
    i += 1