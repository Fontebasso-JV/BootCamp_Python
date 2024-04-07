operacao = input('Digite o simbolo da operação desejada  ( "+" , "-" ,  "/" , "*")')

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o primeiro numero: '))

try:
    if isinstance(num1,int)  or isinstance(num2,int):
        if operacao in ('+','-','/','*'):
            if operacao == '+':
                resultadocalc = num1 + num2
            elif operacao == '-':
                resultadocalc = num1 - num2
            elif operacao == '*':
                resultadocalc = num1 * num2
            elif operacao == '/':
                resultadocalc = num1 / num2
    else:
        print("Operado inválido ou divisão por zero")
    print(f'O resultado da sua operação é : {resultadocalc}')

except ValueError:
    print(f'Erro: Entrada inválida')