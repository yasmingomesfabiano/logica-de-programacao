#receber a idade 
idade= int(input("Informe a sua idade:"))

#informar se a pessoa pode ou não entrar na festa 

if idade >=18:
   print("você pode entrar!")

if idade <=18:
   print("você não pode entrar!")

if idade >=60:
   print("você não pode entrar!")


#correçao da professora

idade= int(input("Digite sua idade:"))

pode_entrar= idade >=18 and idade <=60

print(pode_entrar)





