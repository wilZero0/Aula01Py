podeDirigir = (input('Você pode Dirigir (Sim) ou (Não)'))
idade = int(input('Digite sua idade'))
if (idade>=18 and podeDirigir=='Sim'):
    print('Liberado')
else:
    print('Não Liberado')