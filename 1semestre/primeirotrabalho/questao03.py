#declarando funçao
def escolha_servico():
    while True:
        print('DiG:')
        print('ICO:')
        print('IPB:')
        print('FOT:')
        servico = input('entre com o tipo de serviço desejado: ')
        if servico == 'DIG':
            return 1.10
        elif servico == 'ICO':
            return 1.00
        elif servico == 'IPB':
            return 0.40
        elif servico == 'FOT':
            return 0.20
        else:
            print('escolha inválida, entre com o tipo do serviço novamente: ')


def num_pagina():
    while True:
        try:
            pagina = int(input('entre com numero de páginas: '))
            if pagina < 20:
                return pagina
            elif pagina >= 20 and pagina < 200:
                return pagina * 0.85
            elif pagina >= 200 and pagina < 2000:
                return pagina * 0.8
            elif pagina >= 2000 and pagina < 20000:
                return pagina * 0.75
            else:
                print('Não aceitamos tantas páginas de uma vez: ')
                print('Por favor, entre com o número de páginas novamente: ')
        except ValueError:
            print('entre com o numero de paginas novamente: ')


def servico_extra():
    while True:
        adicional = int(input('deseja adicionar algum serviço?: '))
        if adicional == 1:
            return 15
        elif adicional == 2:
            return 40
        elif adicional == 0:
            return 0
        else:
            print('Não desejo mais nada: ')


#programa principal
def main():
    print('Seja bem vindo a Copiadora da Rayssa Almeida')
    valorserv = escolha_servico()
    numeropagina = num_pagina()
    extra = servico_extra()
    total = (valorserv * numeropagina) + extra
    print(' total: ' + str(total) + ' servico: ' + str(valorserv) + ' pagina: ' + str(numeropagina) + ' extra: ' + str(extra))
    print('Obrigada, volte sempre!')
#tive que usar a funçao str() , pois estava dando erro.
if __name__ == "__main__":
    main()
