#IDENTAÇÃO E BLOCOS
def sacar(valor: float):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire seu dinheiro na boca do caixa.")
    
    print("Obrigado por ser nosso cliente, tenha um bom dia")
    print()

def depositar(valor: float):
    saldo = 500
    saldo += valor
    print(f'Seu saldo é de {saldo}')

sacar(100)
depositar(200)

#ESTRUTURAS CONDICIONAIS
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE: 
    print("Menor de idade, não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

else: 
    print("Menor de idade, não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer apenas as aulas teóricas")
else: 
    print("Menor de idade, não pode tirar a CNH")


#IF ANINHADO
conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial.")
    else:
        print("Não foi possível realizar o saque!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
else:
    print("Sistema não reconhece seu tipo de conta, entre em contato com seu gerente.")


#IF TERNÁRIO
status = "Sucesso" if saldo <= saque else "Falha"

print(f'{status} ao realizar o saque!')


#ESTRUTURAS DE REPETIÇÃO
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha

# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")


#WHILE
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")


#BREAK
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue

#     print(numero, end=" ")