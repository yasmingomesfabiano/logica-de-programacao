i = 1
while i <5:
    print(i)
    i+=1 #i = i+1


i = 0

while i <3:
    print("Olá")
    i+=1


#while: usa quando quer repertir o código ENQUANTO a condição for verdadeira
#quando usar= quando não se conhece o numer previamente.
#for: quando se sabe o número de repetições, ou quando interar sobre 
#uma sequência.

alunos= ["fulana","betrano","ciclano"]

for aluno in alunos: #para elemento in vetor
    print(f"aluno:{aluno}")
#para cada aluno, dentro de alunos faça:

frutas=["morango","abacate","laranja"]
for fruta in frutas:
    print(f"Fruta:{fruta}")

#tabuada
numero= int(input("Digite um número para ver a tabuada;"))
print(f"Tabuada do {numero}:")
for i in range(1,11): #range:sequência de números inteiros. range(start, stop)
    resultado= numero*i
    print(f"{numero}x{i}={resultado}")