# Cria uma lista vazia para guardar os numeros
numeros = []

# Pede os numeros até o usuario digitar 'sair'
entrada = input("Digite um numero ou 'sair' para parar: ")
while entrada != 'sair':
    # Converte para inteiro e guarda na lista
    numeros.append(int(entrada))
    # Pede o próximo numero
    entrada = input("Digite um númeroou 'sair' para parar: ")
    
#Mostra apenas os numeros pares 
print('Numeros pares digitados: ')
for numero in numeros:
    if numero % 2 == 0:
        print(numero)