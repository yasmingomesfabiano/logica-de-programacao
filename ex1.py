nome=input("Digite seu nome:")
senha=input("Digite sua senha:")

if nome==senha:
    print("a senha não pode ser o mesmo que o nome")
    senha_=input("Crie outra senha:")
    print("Cadastro conclído!")
    
else:
    print("Cadastro conclído!")

#versão da prof

while True:
    nome=input("Digite seu nome:")
    senha=input("Digite sua senha:")

    if senha.lower()==nome.lower():
        print("Erro: a senha não pode ser igual ao nome do usuário. Tente novamente!")
    else:
        print("Cadastro realizado com sucesso!")
        break