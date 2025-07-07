#somar digitos <100

numero= int(input("Digite o número menor que 100:  "))

if numero >=100:
   print ("O número deve ser menor que 100.")

else:
   unidade_dezena= numero //10 #pega a dezena
   unidade_milhar= numero %10  #pega a unidade

   soma=unidade_dezena + unidade_milhar
   print(f"soma:{soma}")

