""" 
controle_biblioteca: dict = {
   "Livro_01": { "Titulo": "Game Of Thrones",
    "Autor": "Estagiário",
    "Ano": 2005},

   "Livro_02": { "Titulo": "Game Of Thrones2",
    "Autor": "Estagiário",
    "Ano": 2007},
}

##for key,value in controle_biblioteca.items():
 #   print(f'{key}: {value}')

controle_biblioteca2: dict = {
   "Titulo": "Game Of Thrones",
    "Autor": "Estagiário",
    "Ano": 2005

}

print(controle_biblioteca["Livro_02"]["Ano"])
print(controle_biblioteca["Livro_01"]["Ano"])

print(controle_biblioteca2.values)

lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[key] for key in lista_compras)
print(f"Preço total: {total}") """


""" idades = [22, 15, 30, 17, 18]

idade_filtrada = []
for i in idades:
    if i >= 18:
        idade_filtrada.append(i)

print(idade_filtrada) """



""" produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

print(produtos)

# Atualizar o preço do produto com id 2 para 90

for i in produtos:
    if i["id"] == 2:
        i["preço"] = 90

print(produtos) """


""" estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

for produto in estoque.values():
    if produto > 0:
        print(produto) """


estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}
estoque2 = {produto: quantidade in estoque.items()}

print(estoque_positivo)
