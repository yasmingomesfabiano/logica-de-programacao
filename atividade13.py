numero=int(input('Digite um número: '))
if numero == 0:
    print('Erro!')
    exit()
    
    
soma = sum(int(digito) for digito in str(numero))
print(soma)

