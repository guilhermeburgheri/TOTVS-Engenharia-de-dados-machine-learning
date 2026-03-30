produto_1 = 10
produto_2 = 20
produto_3 = 25
produto_4 = 35
produto_5 = 35

#OPERADORES ARITMÉTICOS
print(produto_1 + produto_3)
print(produto_3 + produto_4)
print(produto_4 - produto_2)
print(produto_3 - produto_1)
print(produto_4 / produto_2)
print(produto_3 / produto_1)
print(produto_4 // produto_2)
print(produto_3 // produto_1)
print(produto_4 * produto_2)
print(produto_3 * produto_1)
print(produto_4 % produto_2)
print(produto_3 % produto_1)
print(produto_4 ** produto_2)
print(produto_3 ** produto_1)
print()

#OPERADORES DE COMPARAÇÃO
print(produto_1 == produto_2)
print(produto_4 == produto_5)
print(produto_1 != produto_2)
print(produto_4 != produto_5)
print(produto_4 > produto_2)
print(produto_4 < produto_2)
print(produto_1 <= produto_2)
print(produto_4 >= produto_5)
print()

#OPERADORES DE ATRIBUIÇÃO
produto_1 = 15
produto_2 += 15
produto_3 -= 15
produto_4 /= 5
produto_5 //= 5
print(produto_1)
print(produto_2)
print(produto_3)
print(produto_4)
print(produto_5)

produto_1 *= 5
produto_2 %= 5
produto_3 **= 5
print(produto_1)
print(produto_2)
print(produto_3)
print()

#OPERADORES LÓGICOS
produto_1 = 10
produto_2 = 20
produto_3 = 25
produto_4 = 35
produto_5 = 35

exp_1 = produto_1 >= produto_2 or produto_4 >= produto_5
exp_2 = produto_1 >= produto_2 and produto_4 >= produto_5
print(exp_1)
print(exp_2)
print()

#OPERADORES DE IDENTIDADE
saldo = 1000
limite = 500
print(saldo is limite)
print(saldo is not limite)
print()

#OPERADORES DE ASSOCIAÇÃO
frutas = ["limão", "uva"]
curso = "Curso de Python"

print("laranja" in frutas)
print("laranja" not in frutas)
print("Python" in curso)
