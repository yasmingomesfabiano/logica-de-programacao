#Acessar os elementos 
vetor=["a", "b", "c", 1, 2, 3]
primeiro=vetor[0]#"a"
#vetor é ma variavel mais cpomplexa que dá para colocar mais de um valor.
#fatiamento(slicing)= pega uma faixa de elemetos 

sub_vetor= vetor[1:4]
print(sub_vetor)

#adicionar elementos
vetor.append("d")#adiciona elemento ao final do valor
print(vetor)

#adicionar vários elementos de uma vez

vetor.extend([4,5])

#remover elementos
vetor.remove("b")

#remover o elemento por índice(posição)
del vetor[2]
print(vetor)

#atualizar elementos 
#atribui um nvo valor para a posição específica
vetor[0]= "JLR"
print(vetor)

#print(vetor)
#remove ele mento pela posição
frutas=["morango","maça", "uva", "jaca"]
frutas.pop(2)
print(frutas)

#len (IMPORTANTE)= LENGTH
tamanho_vetor= len(vetor)
print(vetor)
print(tamanho_vetor)

#odernção 
#sort= ele colocou em ordem alfabética/crescente 
matriculas=["yasmin g", "yasmim s"]
vetor.sort()
print(matriculas)

#cria nova lista ordenadas
novo_vetor= sorted(matriculas)
print(matriculas)

#interação: percorre os elementos
for estudante in matriculas:
    print(estudante)

#for é um laço de repetição

novo_vetor= sorted(matriculas)
print(novo_vetor)

#interação: percorre os elementos 
for estudante in matriculas:
    print (estudante)

#dividir strings em palavras 
frase= "python é muito bom!"
palavras = frase.split()
print(palavras)

#juntar palavras em string
nova_frase= " ".join(palavras)
print(nova_frase)

#operações matemáticos em vetores numericos 
vetor_numerico= [1,2,3,4]
for i in range(len(vetor)):
    vetor_numerico [i] *=2 #vetor_numerico[i]= vetor+_numerico[2]*2
print(vetor_numerico)