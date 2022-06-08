import random
banco_de_palavras = ['futebol','ginastica-artistica','natacao','volei','esgrima']
palavra_secreta = random.choice(banco_de_palavras).upper()
acertos = 0
erros = 0
letras_acertadas = '-'
letras_erradas = ''.upper()
forca = ['''\033[m
|>----
|    |
|
|
|
|''','''\033[33m
|>----
|    |
|    o
|
|
|''','''\033[32m
|>----
|    |
|    o
|    |
|
|''','''\033[36m
|>----
|    |
|    o
|   /|
|
|''','''\033[34m
|>----
|    |
|    o
|   /|\\
|
|''','''\033[35m
|>----
|    |
|    o
|   /|\\
|   /
|''','''\033[31m
|>----
|    |      GAME OVER
|   \033[37m o\033[31m
|   \033[37m/|\\\033[31m
|   \033[37m/ \\\033[31m
|''']

while acertos != len(palavra_secreta) and erros != 7:
    if erros == 0:
        print(forca[0])
    elif erros == 1:
        print(forca[1])
    elif erros == 2:
        print(forca[2])
    elif erros == 3:
        print(forca[3])
    elif erros == 4:
        print(forca[4])
    elif erros == 5:
        print(forca[5])
    elif erros == 6:
        print(forca[6])
    else:
        print(forca[7])

    for letra in palavra_secreta:
         if letra in letras_acertadas:
             print(f' {letra} ', end='')
         else:
             print(' _ ',end='' )
    print(f'\nErros: {letras_erradas} ')

    letra = input('Digite a letra: ').upper()
    if letra in letras_erradas:
        print('Essa letra ja foi, toma um ponto ai de graça')
        letras_erradas = letras_erradas[:-1]

    if letra in palavra_secreta:
        letras_acertadas += letra
        acertos += palavra_secreta.count(letra)
        if acertos == len(palavra_secreta):
            print(f'\033[33m\o/UHUUUUUUUUL VOCÊ ACERTOU A PALAVRA É {palavra_secreta}\o/')
            break
    else:
        letras_erradas += letra
        erros += 1


