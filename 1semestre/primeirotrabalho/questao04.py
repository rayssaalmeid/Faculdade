print("Bem Vindo a Livraria da Rayssa Almeida")
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
       print("1 consultar todos")
       print("2 consultar por id")
       print("3 consultar por autor")
       print("4 retornar ao menu")
       resposta = input("qual opçao deseja: ")
       if resposta == 1 :
         for livro in lista_livro:
           print(livro)
       elif resposta == 2 :
           id_buscado = input("digite o id do livro: ")
           for livro in lista_livro:
              if id_buscado == livro["id"]:
                  print(livro)
       elif resposta == 3 :
           autor_buscado = input("digite o autor do livro: ")
           for livro in lista_livro:
               if autor_buscado == livro["autor"]:
                   print(livro)
       elif resposta == 4 :
           break
       else:
           print('opçao invalida')
def remover_livro():
    while True:
      id_removido = input("digite o id do livro a ser removido ")
      for livro in  lista_livro:
          if id_removido == livro['id']:
              lista_livro.remove(livro)
#codigo principal












