######################################### LISTA DE EXERCÍCIO 03 #################################################
#################################################################################################################
# 01
#################################################################################################################

user = " "
while user != "admin":
    user = input("Digite o nome do usuário: ")  
print("Acesso permitido")

# É necessário dar um valor para entrar em while, enquanto user não for admin ele continuará perguntando o usuário

#################################################################################################################
#02
#################################################################################################################

user = int("-1")
while user < 0:
    user = int(input("Digite o número do usuário: "))
print("Valor aceito!")

#É necessário dar o valor que inicia o loop que não equivala ao resultado que precisamos para finalizar o while.
# While continua até o usuário dar um número maior que zero

#################################################################################################################
# 03
#################################################################################################################

saldo = 1000.0


print(f'Seu saldo e {saldo:.2f}')
while saldo > 0:
    saque = float(input('Valor do saque: '))
    if saque <=0:
        print('Valor de saque invalido')
    elif saque > saldo:
        print('Saldo insuficiente')
    else:
        saldo -= saque
        print(f'Restante na conta {saldo:.2f}')
        
print('Saldo zerado')

# O saldo é 1000 reais, enquanto saldo for maior que zero ele continuará informando o saldo com .2f sendo para limitar em 2 casas
# Enquanto saldo for maior que 0 ele pedirá o valor do saque, se ele for maior que zero mas maior que o saldo ele será inválido
# E por fim, se ele for menor que saldo e maior que zero, o sistema fará a subtração do saque no saldo, informando o restante na conta.
    
#################################################################################################################    
#04
#################################################################################################################

resposta = "s"
quantidade = 0
while resposta == "s":
    idade = int(input("Digite uma idade: "))
    quantidade += 1
    resposta = input("Deseja continuar? s/n")
print(f"Quantidade de idades informadas é de: {quantidade}")

# O código continuará rodando em loop, pedindo uma idade e contando quantadas idades foram informadas até que a resposta seja n
    
#################################################################################################################
#05
#################################################################################################################

pin = 0000
tentativa = 0

while pin != 4321:
    pin = int(input('Digite o PIN: '))
    tentativa +=1
    
    if tentativa > 3:
        print('Cartao bloqueado')
        break
else:
    print('Acesso liberado')

# Enquanto pin não for 4321 ele pedirá para digitar pin até a terceira tentativa, se na terceira não for correto a saída seja cartão bloqueado e finalizará
# Caso pin seja informado antes da 3 tentativa, será acesso liberado.

#################################################################################################################
#06
#################################################################################################################

opcao = 4

while opcao != 3:
    print(" ")
    print("**MENU**")
    print("1-SOMAR")
    print("2-SUBTRAIR")
    print("3-SAIR")
    opcao = int(input(" "))
    
    if opcao == 1:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número "))
        soma = num1 + num2
        print(f"O resultado da soma dos numeros é de: {soma}")
        
    elif opcao == 2:
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite outro número "))
        subtrair = num1 - num2
        print(f"O Resultado da subtração dos números é: {subtrair}")
        
else:
    print("SAIR")
    
# Para este código primeiro ele apresentará as opções, sendo soma, subtração e sair e pedirá uma próxima ação
# Se a resposta for 1, ele pedirá 2 números e irá fazer a soma deles, se a resposta for 2 ele pedirá 2 números e fará subtração, se 3 ele apenas encerra.
    
