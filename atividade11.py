#ler salário e valor
salario=float(input('Informe seu salário: '))
emprestimo=int(input('Informe o valor da prestação: '))

if salario*0.2 > emprestimo:
    print('Empréstimo concedido!')

else:
    print("Empréstimo não concedido!")
