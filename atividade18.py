distancia=float(input('Informe a distância pecorrida em Km: '))
consumo=float(input('Informe o consumo de gasolina a cada Km/l: '))
 
consumidos=distancia/consumo
print(f"Consumo do carro: {consumo:.2f} km/l")
if consumo < 8:
    print('Venda o carro!')
    
elif 8 <= consumo < 12:
    print("Econômico!")

else:
    print('Super econômico!')