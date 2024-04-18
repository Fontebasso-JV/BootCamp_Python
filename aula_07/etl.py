
import csv

path_arquivo = "vendas.csv"

##########################################
##FUNÇÃO QUE FAZ A LEITURA DO ARQUIVO CSV
##########################################

def read_csv(nome_arquivo: str) -> list[dict]:
    lista = []
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


##################
##TRANSFORMAÇÃO
#################

def processar_dados(lista: list[dict]) -> list[dict]:
    categoria = []
    for produtos in lista:
        if produtos.get("entregue") == "true":
            categoria.append(produtos)
    return categoria


print(processar_dados(read_csv(path_arquivo)))