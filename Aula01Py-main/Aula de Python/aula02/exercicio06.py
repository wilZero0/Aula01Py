# 1=Branco
# 2=verde
# 3=vermelho
print('Votação')

nome = input('Digite seu nome: ')
voto = int(input('Digite seu voto: '))

if(voto==1):
    print(f'{nome} Branco')
elif(voto==2):
    print(f'{nome} Votou no Verde')
elif(voto==3):
    print(f'{nome} Votou no Vermelho')
else:
    print (f'{nome} Voto errado')
print('Obrigado por votar')