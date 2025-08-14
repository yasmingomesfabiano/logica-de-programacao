#receber a altura e o sexo
altura=float(input('Informe sua altura: '))
sexo=input('Informe seu sexo F ou M:')

if sexo == 'F':
    conta=(62.1*altura)-44.7
    print(f'Seu peso ideal é {conta}')
    
elif sexo == 'M':
    conta=(72.7*altura)-58
    print(f'Seu peso ideal é {conta}')

else:
    print('Erro, tente novamente!')
    
    