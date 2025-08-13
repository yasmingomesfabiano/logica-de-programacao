try:
    x = int(input("Digite um número: "))
    print(10 / x)
except ZeroDivisionError:
    print("Não dá para dividir por zero!")
finally:
    print("Fim do código")