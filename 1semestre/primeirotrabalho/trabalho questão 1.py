print('seja bem vindo a loja da rayssa almeida')
#colocando as variaveis
#decidi colocar int, estudo por fora..
valor = int(input('valor do produto: '))
quantidade = int(input('quantidade do produto: '))
desconto = 0
#agora multiplicando
valorsomado = valor * quantidade
#aplicando os descontos
if valorsomado < 2500:
    print('valor da compra', valorsomado)
#desconto 4%
elif valorsomado >= 2500 and valorsomado < 6000:
    print('você ganhou desconto de 4%!')
    desconto = (4/100) * valorsomado
    print('valor SEM desconto: ', valorsomado)
    print('valor COM desconto: ', valorsomado - desconto)
#desconto 7%
elif valorsomado >= 6000 and valorsomado < 10000:
    print ('você ganhou desconto de 7!%')
    desconto = (7/100) * valorsomado
    print('valor SEM desconto: ', valorsomado)
    print('valor COM desconto: ', valorsomado - desconto)
else:
    print ('você ganhou desconto de 11!%')
    desconto = (11/100) * valorsomado
#recebendo desconto

    print('valor SEM desconto: ', valorsomado)
    print('valor COM desconto: ', valorsomado - desconto)
print('obrigada,volte sempre!')