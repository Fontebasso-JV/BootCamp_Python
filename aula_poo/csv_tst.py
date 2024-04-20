import pandas as pd

df = pd.read_csv('./exemplo.csv')

df_filtrado = df[df["estado"] == 'SP']

print(df)
print(df_filtrado)


class CsvProcessor:
    def __init__(self,file_path: str):
        self.file_path = file_path
        self.df = None


        def carregar_csv(self):
            self.df = pd.read_csv(self.file_path)


        
        def filtrar_por(self,collumn,atributo):
            return self.df[self.df[collumn] == atributo]
        

arquivo_csv = './exemplo.csv'
filtro = 'estado'
limite = 'SP'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(filtro,limite))