#lista=Coleção ordenada e mutábel de elementos. Pode ser modificada
#consigo excluir, adicionar e atualizar uma lista
frutas=['maça', 'banana', 'laranja']
print(frutas)

#adiciona item na lista 
frutas.append('uva')
print(frutas)

#tupla: coleção ordenada, mas IMUTÁVEL (não pode ser alterada após criada)
coordenadas= (10.0,20.0)
print(coordenadas)

#dicionário: coleção não ordenada de oares chaves-valor.
aluno={
    'nome': 'Mauro',
    'idade': 25,
    'curso': 'pscicologia'
}
print(aluno)
print(aluno['nome'])

aluno ['idade'] = 21
print(aluno)
