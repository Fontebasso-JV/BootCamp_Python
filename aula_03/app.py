""" x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


try:
    print(0 / 0)
except:
    e = TypeError
    print(e)  """

""" # Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
 """
# Measure some strings:
nome = ['Luciano']
for letra in nome:
    print(letra)


a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

texto = "a raposa marrom salta sobre o cachorro preguiçoso"
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)


# Measure some strings:
dic_palavras = {}

words = ['cat', 'window', 'defenestrate']
for w in words:
    if w not in dic_palavras:
        dic_palavras[w] = len(w)
    else:
         dic_palavras[w] = +1

print(dic_palavras)