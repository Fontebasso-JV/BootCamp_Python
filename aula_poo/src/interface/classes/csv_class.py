import pandas as pd

class CsvProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None
        self.df_filtrado = None
    
    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
    
    def filtrar_por(self, collumn, atributo):
         self.df_filtrado = self.df[self.df[collumn] == atributo]
         return self.df_filtrado
    
    def sub_filtro(self,collumn,atributo):
        return self.df_filtrado[self.df_filtrado[collumn] == atributo]