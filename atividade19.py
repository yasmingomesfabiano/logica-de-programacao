codigo=int(input('Digite o código do produto: '))
quantidade=int(input('Informe a quantidade: '))

if codigo == 100:
    calculo= 1.20*quantidade
    print(f'você pediu {quantidade} cachorro(s) quente(s), no valor de {calculo:.2f}')

elif codigo == 101:
    calculo= 1.30*quantidade
    print(f'você pediu {quantidade} bauru(s) simples, no valor de {calculo:.2f}')
 

elif codigo == 102:
    calculo= 1.50*quantidade
    print(f'você pediu {quantidade} bauru(s) com ovo, no valor de {calculo:.2f}')
    

elif codigo == 103:
    calculo= 1.20*quantidade
    print(f'você pediu {quantidade} hamburguer(s), no valor de {calculo:.2f}')
    

elif codigo == 104:
    calculo= 1.70*quantidade
    print(f'você pediu {quantidade} cheeseburguer(s), no valor de {calculo:.2f}')
    

elif codigo == 105:
    calculo= 2.20*quantidade
    print(f'você pediu {quantidade} suco(s), no valor de {calculo:.2f}') 
    

elif codigo == 106:
    calculo= 1.00*quantidade
    print(f'você pediu {quantidade} refrigerante(s), no valor de {calculo:.2f}') 
    
else:
    print('Aconteceu algum erro, tente novamente!') 
