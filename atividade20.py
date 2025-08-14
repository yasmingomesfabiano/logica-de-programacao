custo=float(input('Informe o custo de fábrica: '))

if custo < 12.000:
    custo_final= custo + (custo* 0.05)
    print(f'o custo ao consumidor é: R${custo_final:.3f}') 
    
    
elif 12.000 <= custo <= 25.000:
    custo_final=custo + (custo*0.10) + (custo*0.15)
    print(f'o custo ao consumidor é: R${custo_final:.3f}')
    
    
else:
    custo_final=custo + (custo*0.15) + (custo*0.20)
    print(f'o custo ao consumidor é: R${custo_final:.3f}')
    