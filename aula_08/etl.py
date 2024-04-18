import pandas as pd
import os
import glob



# FUNCÃO QUE LE E CONSOLIDA OS JSON

def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list,ignore_index=True)
    return df_total




# UMA FUNCAO QUE TRANSFORMA

def calcular_kpi_total(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df




# UMA FUNCAO QUE DA LOAD EM CSV OU PARQUET


def carregar_dados(df: pd.DataFrame, format_saida: list):

    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv")
        if formato == 'parquet':
            df.to_parquet("dados.parquet")




# PIPELINE CLIENTE

def pipeline_calcular_kpi_de_vendas_consolidado(pasta: str, formato_de_saida: list):

    data_frame = extrair_dados(pasta)
    data_frame_calc = (calcular_kpi_total(data_frame))
    carregar_dados(df=data_frame_calc,format_saida=formato_de_saida)


# RODANDO SOMENTE NA MAIN

if __name__ == "__main__":
    pasta_argumento = 'data'
    data_frame = extrair_dados(pasta_argumento)
    data_frame_calc = (calcular_kpi_total(data_frame))
    formato_de_saida: list = ["csv","parquet"]
    carregar_dados(df=data_frame_calc,format_saida=formato_de_saida)