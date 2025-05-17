print("Bem Vindo a Livraria da Rayssa Almeida")
print("----------------------------------------------\n--------------- MENU PRINCIPAL ---------------")
lista_livro = []
id_global = 0
def cadastrar_livro(id):
   n = input("por favor entre com o nome do livro: ")
   a = input("por favor entre com o autor do livro: ")
   e = input("por favor entre com editora do livro: ")
   #criando dicionario
   livro = {
       "nome": n,
       "id": id,
       "autor": a,
       "editora": e,
   }
   lista_livro.append(livro)
def consultar_livro():
   while True:
       print("Escolha a opção desejada:")
       print("1 consultar todos")
       print("2 consultar por id")
       print("3 consultar por autor")
       print("4 retornar ao menu")
       resposta = int(input())
       if resposta == 1 :
            for livro in lista_livro:
                print("numero do id: " + str(livro["id"]))
                print("nome do livro: " + livro["nome"])
                print("nome do autor: " + livro["autor"])
                print("nome da editora: " + livro["editora"])
       elif resposta == 2 :
           id_buscado = int(input("digite o id do livro: "))
           for livro in lista_livro:
              if id_buscado == int(livro["id"]):
                  print("numero do id: " + str(livro["id"]))
                  print("nome do livro: " + livro["nome"])
                  print("nome do autor: " + livro["autor"])
                  print("nome da editora: " + livro["editora"])
       elif resposta == 3 :
           autor_buscado = input("digite o autor do livro: ")
           for livro in lista_livro:
               if autor_buscado == livro["autor"]:
                   print("numero do id: " + str(livro["id"]))
                   print("nome do livro: " + livro["nome"])
                   print("nome do autor: " + livro["autor"])
                   print("nome da editora: " + livro["editora"])
       elif resposta == 4 :
           break
       else:
           print('opçao invalida')
def remover_livro():
    while True:
        id_removido = int(input("digite o id do livro a ser removido "))
        for livro in  lista_livro:
            if id_removido == int(livro['id']):
                lista_livro.remove(livro)
        break
#codigo principal
while True:
    print("Escolha a opção desejada")
    print("1 - Cadastrar livro")
    print("2 - Consultar livros ")
    print("3 - Remover livro")
    print("4 - Sair")
    resposta  = int(input())
    if resposta == 1:
        print("----------------------------------------------\n------------ MENU CADASTRAR LIVRO ------------")
        id_global = int(input("Id do Livro: "))
        cadastrar_livro(id_global)
    elif resposta == 2:
        print("----------------------------------------------\n------------ MENU CONSULTAR LIVRO ------------")
        consultar_livro()
    elif resposta == 3:
        print("----------------------------------------------\n------------ MENU REMOVER LIVRO --------------")
        remover_livro()
    elif resposta == 4:
        break
    else:
        print("Opção invalida")






