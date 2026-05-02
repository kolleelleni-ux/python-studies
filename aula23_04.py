#######################################

nome = 'Marina'
curso = 'Introdução a Programação de Computadores'

print(nome[0])
print(nome[-1])

#######################################

nome = 'Danielle'

maiusculo = nome.upper()
minusculo = nome.lower()

print(nome.upper())
print(nome.lower())
print(maiusculo)
print(minusculo)

tamanho = len(nome)
print(tamanho)

#######################################

frase = "O Neymar vai ser convocado para a Copa Do Mundo 2026"
texto_corrigido = (frase.replace("vai", "não vai"))

print(texto_corrigido)

#######################################

nome = "Danielle"
cidade = "Maringá"
mensagem = f"A {nome} mora em {cidade}."

print(mensagem)
len(nome)

#######################################

notas = [8.5, 7.0, 9.2, 6.8]
nomes = ["Ana", "Carlos", "Julia", "Pedro"]
idades = [18, 19, 20, 21]

print(notas)
print(nomes)
print(idades)

#######################################

nomes = ["Ana", "Carlos", "Julia", "Pedro"]
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])

#######################################

nomes = ["Ana", "Carlos", "Julia", "Pedro", "Julia"] # nome = objeto, nomes = vetor. Vetor é um conjunto de objetos

nomes[2] = "Julio"
print(nomes)

#######################################

nomes = ["Ana", "Carlos", "Julia", "Pedro"]
nomes.insert(1, "Bruno")

print(nomes)

#######################################

nomes = ["Ana", "Carlos", "Julia", "Pedro"]
nomes.remove("Ana")

print(nomes)

#######################################

nomes = ["Ana", "Carlos", "Julia", "Pedro"] # append sempre vai para o final, não é necessário declarar posição
nomes.append("Carlos")

print(nomes)

#######################################

nomes = ["Misael", "Lucas", "George", "Thulio"]

for nome in nomes:
  print("Aluno:", nome)
  
#######################################

numeros = [1, 2, 3, 4, 5]

for numero in numeros:
  print(numero * 2)
  
#######################################

produtos = ["Teclado", "Mouse", "Headset", "Monitor", "CPU"]

for i in produtos:
  print(f"Produtos cadastrados: {i}")
  print("Produtos cadastrados:", i)

#######################################

compras = ["Arroz", "Feijão", "Leite"]

print("Lista inicial:", compras)

compras.append("Café")
compras.append("Chá")

print("Lista inicial:", compras)

#######################################

nomes = ["Ana", "João", "Carlos", "Fernando", "Pedro"]

print(nomes[0], nomes[4])

nomes[0] = "Aline"
print(nomes)

nomes.append("Marcos")
print(nomes)

#######################################

nomes = ["Ana", "João", "Carlos", "Fernando", "Pedro"]

for i in nomes:
  print(i)
  
#######################################

coordenadas = (10 ,20)
dias_semana = ("seg", "ter", "qua", "qui", "sex")
print(coordenadas)
print(dias_semana)

