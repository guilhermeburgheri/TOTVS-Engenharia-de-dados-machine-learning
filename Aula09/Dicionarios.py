pessoa = {"nome": "Guilherme", "idade": 24}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=24)
print(pessoa)

pessoa["telefone"] = "1234-5678"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)


dados = {"nome": "Guilherme", "idade": 24, "telefone": "1234-5678"}

print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 24
print(dados["telefone"])  # "1234-5678"

dados["nome"] = "Giovanna"
dados["idade"] = 21
dados["telefone"] = "8765-4321"

print(dados)  # {"nome": "Maria", "idade": 21, "telefone": "8765-4321"}


#ANINHADOS
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "8765-4321"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "1234-1234"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "5678-5678"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "8765-4321"
print(telefone)


#ITERANDO
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "8765-4321"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "1234-1234"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "5678-5678"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)


#CLEAR
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "8765-4321"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "1234-1234"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "5678-5678"},
}

contatos.clear()
print(contatos)  # {}


#COPY
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "1234-5678"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}


#FROMKEYS
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "1234-5678"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}


#GET
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "1234-5678"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}


#ITEMS
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "1234-5678"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}


#KEYS
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)


#POP
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '1234-5678'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)


#POPITEM
contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '1234-5678'})
print(resultado)

# contatos.popitem()  # KeyError


#SETDEFAULT
contato = {"nome": "Guilherme", "telefone": "1234-5678"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '1234-5678'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '1234-5678', 'idade': 24}


#UPDATE
contato = {"nome": "Guilherme", "telefone": "1234-5678"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '1234-5678'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '1234-5678', 'idade': 28}


#VALUES
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "8765-4321"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "1234-1234"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "5678-5678"},
}

resultado = (
    contatos.values()
)  # dict_values([{'nome': 'Guilherme', 'telefone': '1234-5678'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])  # noqa
print(resultado)


#IN
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "8765-4321"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "1234-1234"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "5678-5678"},
}

resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

resultado = "megui@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)


#DEL
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "1234-5678"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "8765-4321"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "1234-1234"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "5678-5678"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '8765-4321'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '5678-5678'}}  # noqa
print(contatos)