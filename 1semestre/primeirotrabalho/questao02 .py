print('Seja bem vindo a açaiteria da Rayssa Almeida')
print("--------------------Cardápio-------------------- \n------------------------------------------------ \n---| Tamanho  | Cupuaçu (CP)  |  Açaí (AC)  |--- \n---|    P     |   R$ 9.00     |  R$ 11.00   |--- \n---|    M     |   R$ 14.00    |  R$ 16.00   |--- \n---|    G     |   R$ 18.00    |  R$ 20.00   |--- \n------------------------------------------------ ")
#variaveis
sabor = 'sabor'
tamanho = 'tamanho'
acumulador = 0
resposta = 'r'
# começo da repetiçao
while True:
    sabor = input('entre com sabor desejado: ')
    tamanho = input('entre com tamanho desejado: ')
    #validando sabor
    if sabor == 'CP':
        #validando tamanho
        if tamanho == 'P':
           acumulador = acumulador + 9
           print('você pediu um cupuaçu no tamanho P: R$9.00')
        elif tamanho == 'M':
           acumulador = acumulador + 14
           print('você pediu um cupuaçu no tamanho M: R$14.00')
        elif tamanho == 'G':
            acumulador = acumulador + 18
            print('você pediu um cupuaçu no tamanho G: R$18.00')
        else:
            print('tamanho inválido, tente novamente')
            continue
    elif sabor == 'AC':
        # validando tamanho
        if tamanho == 'P':
            acumulador = acumulador + 11
            print('você pediu um açai no tamanho P: R$11.00')
        elif tamanho == 'M':
            acumulador = acumulador + 16
            print('você pediu um açai no tamanho M: R$16.00')
        elif tamanho == 'G':
            acumulador = acumulador + 20
            print('você pediu um açai no tamanho G: R$20.00')
        else:
            print('tamanho inválido, tente novamente')
            continue
    else:
        print('sabor inválido, tente novamente')
        continue
    resposta = input('Deseja mais alguma coisa:? ')
    #validando resposta
    if resposta == 'N':
        print('valor total a ser pago:', acumulador)
        break

