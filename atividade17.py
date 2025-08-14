menu=int(input('Digite a opção desejada:\n1- soma de 2 números:\n2- diferença entre 2 números\n3- produto entre 2 números\n4- divisão entre 2 números\n'))
if menu == 1:
    numero1=int(input('Digite o primero número: '))
    numero2=int(input('Digite o segundo número: '))
    
    soma= sum(numero1,numero2)
    print(soma)
    
elif menu == 2:
    numero1=int(input('Digite o primero número: '))
    numero2=int(input('Digite o segundo número: '))
    
    maior=max(numero2,numero1)
    menor=min(numero1,numero2)
    
    print(f'número {maior} é o maior, e o {menor} é o menor.')

elif menu ==3:
    numero1=int(input('Digite o primero número: '))
    numero2=int(input('Digite o segundo número: '))
    
    multiplicacao=numero1*numero2
    print(multiplicacao)
    
elif menu == 4:
    numerador=int(input('Digite o primero número: '))
    denominador=int(input('Digite o segundo número: '))
    if denominador ==0:
        print('erro, o denominador não pode ser zero.')
    else:
        divisao= numerador/denominador 
        print(divisao) 
        
else:
    print('erro, tente novamente!')  
    
    