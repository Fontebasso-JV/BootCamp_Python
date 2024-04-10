""" qtd_alunos = int(input())

if qtd_alunos == 0:
    print("NÃO HOUVE PROCESSAMENTO")

else:
    qtd_alunos2 = 0
    soma_media = 0
    while qtd_alunos2 < qtd_alunos:
        media = float(input())
        qtd_alunos2 += 1
        soma_media += media

        if media >= 6:
            print("PARABÉNS VOCÊ ESTÁ APROVADO")

if qtd_alunos2 > 0 and soma_media > 0:
    media_geral = soma_media / qtd_alunos2        
    print(media_geral) """


qtde = int(input())
cont = 0
soma = 0

if qtde == 0:
    print('NÃO HOUVE PROCESSAMENTO')

else:
    while cont < qtde:
        media = float(input())
        soma+=media
        cont+=1

        if media>=6.0:
            print('PARABÉNS VOCÊ ESTÁ APROVADO')

if qtde!=0:
    print(soma/qtde)