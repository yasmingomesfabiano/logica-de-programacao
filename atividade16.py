numero=int(input('Digite um número:'))
if numero %3==0 and numero %5 != 0 :
    print('Esse número é divísivel por três. ')
    
elif numero %5 ==0 and numero %3 != 0:
    print('Esse número é divísivel por cinco. ')
    
else:
    print('O número é divísivel por ambos.')
    