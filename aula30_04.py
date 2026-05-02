#######################################

pais = ["China", "Japão", "Coréia do Sul"]
print(pais)
# Tuplas () são vetores não modificáveis e não alteráveis, lista [] você consegue alterar, adicionar, remover.

#######################################

pais = ("China", "Japão", "Coréia do Sul")
pais.append("Taiwan")

print(pais)

# Gera erro pois a tupla não é alterável.

#######################################

notas = [8.0, 7.5, 9.0, 6.5]

media = sum(notas) / len(notas)
print("Notas:", notas)
print("Média", media)

#######################################

celsius = int(input("Digite a temperatura em celsius: "))
farenhenheit = (celsius * 9/5) + 32

print(farenhenheit)

#######################################

distancia = float(input("Digite a distância em km: "))
metros = distancia * 1000
cm = metros * 100

print(f"A distância em metros é: {metros}")

print(f"A distância em centímetros é: {cm}")

#######################################

massa = 80
velocidade = 12

ec = massa * (velocidade **  2) / 2

print(ec)

#######################################

aluno = {
    "nome": "Maringa",
    "idade": 20,
    "curso": "Computação"
}
aluno["idade"] = 21
aluno["curso"] = "ADS"

aluno["cidade"] = "Maringá"

print(aluno) # Dicionário

#######################################

aluno = {
    "nome": "Danielle",
    "idade": 26,
    "curso": "Análise e Desenvolvimento de Sistemas
}

print(aluno)

#######################################

livro = {
    "título": "Twilight",
    "autor": "Stephenie Meyer",
    "ano": 2005
}

print(livro)

#######################################

aluno = {
    "nome": "Danielle",
    "idade": 26,
    "curso": "Design Gráfico"

}


for i, j in aluno.items():

  print(i, ":", j)   # i e j são indexadores

#######################################

aluno = {
    "nome": "Keiko",
    "idade": 26,
    "curso": "Análise e Desenvolvimento de Sistemas"

}

print(f"Nome do aluno: {aluno["nome"]}")

#######################################

filme = {
    "nome": "A Baleia",
    "ano": 2021
}

filme["genero"] = "Drama"

print(filme)
