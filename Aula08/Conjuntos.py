numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}


#ACESSAR
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])


#ITERAR
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


#UNION
conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)


#INTERSECTION
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)


#DIFFERENCE
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)


#SYMMETRIC
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)


#ISSUBSET
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)


#ISSUPERSET
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)


#ISDISJOINT
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)


#ADD
sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)


#CLEAR
sorteio = {1, 23}

print(sorteio)  # {1,23}

sorteio.clear()

print(sorteio)  # {}


#COPY
sorteio = {1, 23}

print(sorteio)  # {1, 23}

sorteio.copy()

print(sorteio)  # {1, 23}


#DISCARD
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}


#POP
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}


#REMOVE
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}


#LEN
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))  # 10


#IN
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False
