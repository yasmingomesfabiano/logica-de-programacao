
'''def dia_semana(numero):
    match numero:
        case 1: 
            return "Segunda"
        
        case 2: 
            return "Terça"
            
        case 3: 
            return "Quarta"
            
        case 4: 
            return "Quinta"
            
        case 5: 
            return "Sexta"
        
        case 6: 
            return "Sábado"
            
        case 7: 
            return "Domingo"
        
        case _:
            return "dia inválido!"
            
print (dia_semana())'''

def dia_da_semana (numero):
    match numero:
        
        case 1: 
            return "Segunda"
        
        case 2: 
             return "Terça"
            
        case 3: 
            return "Quarta"
            
        case 4: 
            return "Quinta"
            
        case 5: 
            return "Sexta"
        
        case 6: 
            return "Sábado"
            
        case 7: 
            return "Domingo"
        
        case _:
            return "dia inválido!"
    
entrada= int(input("Digite um npumero de 1  7 para o dia da semana:"))

resultado = dia_da_semana(entrada)
print(resultado)


            
            
            
            
        