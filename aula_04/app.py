
###########
##LISTAS []
###########

""" import time

lista_compra : list = []

qtd_adc : int = int(input("Digite Quantos produtos vai inserir: "))

if qtd_adc < 0:
    print("Programa encerrado!")
else:
    include: int = 0
    while include < qtd_adc:
        produto_insert : str = input("Digite o produto a incluir: ")
        include += 1
        lista_compra.append(produto_insert)
        print("Carregando inserção...")
        time.sleep(2)
        print("Produto Incluido!")
    print("Carregando seu carrinho...")
    time.sleep(2)
    print(f'Sua lista de produtos é {lista_compra}') """


#################
##DICIONARIOS {} A DIFERENÇA ENTRE LISTA É QUE A DIC ATRIBUI UMA CHAVE A UM VALOR
#################
import json
import time
produto_01: dict = {
    "nome": "Televisão",
    "quantidade": 40,
    "preco": 3000,
    "disponibilidade": True
}

produto_02: dict = {
    "nome": "Tablet",
    "quantidade": 30,
    "preco": 1500,
    "disponibilidade": True
}


carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

carrinho_json = json.dumps(carrinho)

print(carrinho)
time.sleep(4)
print(carrinho)