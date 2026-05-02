############################################################################################################
############################################## LISTA 02 ####################################################
############################################################################################################
# 1-A

velocidade = float(input("Digite sua velocidade: "))

if 40 <= velocidade <= 80:  
    print ('Velocidade dentro da faixa permitida!')

############################################################################################################
# 1-B

temperatura = float(input('Digite a temperatura: '))

if 18 <= temperatura <= 25:
    print ('A temperatura está agradável')

############################################################################################################
# 1-C

nota = int(input('Digite a nota: '))

if 0 <= nota <= 10:
    print("Nota válida")

############################################################################################################
# 2-A

idade = int(input("Digite a sua idade: "))

if 16 <= idade:
    print("Entrada autorizada")

############################################################################################################
# 2-B

gol = int(input("Digita o número de gols de um jogador: "))

if 0 < gol:
    print("O jogador marcou gold na partida")
    
############################################################################################################
# 2-C

horas = int(input("Digite quantas horas você estudou: "))

if 2 <= horas:
    print ("Meta de estudo atingida")
    
############################################################################################################
# 3-A

valor = float(input("Digite o valor da compra: "))

if 100 <= valor:
    print("Frete grátis")
else:   
    print("Frete cobrado")
    
############################################################################################################
# 3-B

idade = int(input("Digite a sua idade: "))

if 18 <= idade:
    print("Pode dirigir")
else:   
    print("Não pode dirigir")
    
############################################################################################################
# 3-C

nota = int(input("Digite sua nota final: "))
if 6 <= nota:
    print("Aprovado")
else:
    print("Reprovado")
    
############################################################################################################
# 4-A

idade = int(input("Digite a sua idade: "))

if 18 <= idade:
    print("Categoria adulto")
    
elif 12 <= idade:   
    print("Categoria juventil")
    
else:
    print("Categoria infantil")
    
############################################################################################################
# 4-B

idade = int(input("Digite a sua idade: "))

if 60 <= idade:
    print("Idoso")
elif 18 <= idade:
    print("Adulto")
else:
    print("Menor de idade")
    
############################################################################################################
# 4-C

nota = float(input("Digite sua pontuação: "))

if 9 <= nota:
    print("Excelente")
elif 6 <= nota:
    print("Bom desempenho")
else:
    print("Precisa melhorar")
    
############################################################################################################
# 5-A

temperatura = float(input("Digite a temperatura em graus: "))

if temperatura >= 30:
    print("Dia quente")
elif temperatura >= 20:
    print("Dia agradável")
else:
    print("Dia frio")
    
############################################################################################################
# 5-B

preco = float(input("Digite o valor do produto: "))

if preco >= 100:
    print("Produto caro")
elif preco >= 50:
    print("Produto com preço médio")
else:
    print("Produto barato")
             
############################################################################################################
# 5-C

faltas = int(input("Digite a quantidade de faltas do aluno: "))

if faltas ==0:
    print("Frequência perfeita!")
elif faltas <=5:
    print("Boa frequência!")
else:
    print("Frequência baixa!")
