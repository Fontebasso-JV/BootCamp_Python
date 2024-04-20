from src.interface.classes.csv_class import CsvProcessor


arquivo_csv = './exemplo.csv'
filtro = 'estado'
limite = 'SC'

filtro_2 = 'data'
limite_2 = '20/03/2024'

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(filtro,limite))
print(arquivo_CSV.sub_filtro(filtro_2,limite_2))