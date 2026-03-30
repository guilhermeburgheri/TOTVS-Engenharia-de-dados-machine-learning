#DADOS
print(11 + 10) #INT
print(1.5 + 2.5) # FLOAT
print(False) #BOOLEAN
print(True) #BOOLEAN
print("Escrito") #STRING
print()


#MODO INTERATIVO
print("Para acessar o modo interativo, basta digitar 'python' no terminal e pressionar Enter")
print("E para sair basta digitar 'exit()'")
print()


#dir() - Mostra os atributos e métodos disponíveis para um objeto
# print(dir(int)) - Mostra os métodos disponíveis para o tipo int


#help() - Mostra a documentação de um objeto
# print(help(int)) -mMostra a documentação do tipo int


#CONSTANTE E VARIÁVEIS
print("Assim como as variáveis, constantes são utilizadas para armazenar valor, uma constante nasce com um valor e permance com ele até o final da execução do programa, o valor é imutável")
print("mas em python não temos uma maneira de se criar uma constante, devemos deixar avisado aos outros desenvolvedores que a variável é na verdade uma constante")
print("para deixar indicado que é uma constante, devemos criar a variável com letras maiúsculas")
print("Exemplo: PI, GRAVIDADE, etc...")
print()

nome = "Guilherme"
idade = 24
limite_saque_diario = 1000
ESTADOS = ["SP", "RJ", "MG"]

print(nome, "tem", idade, "anos e mora em", ESTADOS[0])
print()


#BOAS PRÁTICAS
print("'snake_case' para variáveis e funções")
print("Escolher nomes sugestivos")
print()


#CONVERSÃO DE TIPOS
print("Em alguns momentos é necessário converter o tipo de uma variável para manipular de forma diferente")
print(int(1.9))
print(int("10"))
print(float("10.10"))
print(str(10.10))
print()


#ENTRADA E SAÍDA DE DADOS
print("Receber e exibir informações para o usuário")
nome = input("Digite seu nome: ")
idade = input("informe sua idade: ")
print(f'Olá, {nome}! Seja bem vindo ao curso de Python!')
print(nome, idade)
print(nome, idade, end=" ... \n")
print(nome, idade, sep="#")
