def perguntar():
    resposta = input("Qual procedimento deseja realizar?" +
                     "\n <I> - Para Inserir um produto" +
                     "\n <P> - Para Pesquisar um produto" +
                     "\n <E> - Para Editar um produto" +
                     "\n <X> - Para Exlcuir um produto" +
                     "\n <L> - Para Listar os produtos"
                     "\n <F> - Para Finalizar o processo: ").upper()
    return resposta


def inserir(dicionario):
    dicionario[input("Digite o código do produto ").upper()] = [input("Digite o nome: ").upper(),
                                                    input("Digite o preço: "),
                                                    input("Digite a validade: ").upper()]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print("Nome....." + lista[0])
        print("Preço...." + lista[1])
        print("Validade." + lista[2])

def editar (dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        edicao = input("Qual elemento deve ser alterado?"
              "\n <N> - Para Nome"
              "\n <P> - Para Preço"
              "\n <V> - Para Validade").upper()

        if edicao == "N": lista[0] = input("Novo Nome: ")
        if edicao == "P": lista[1] = input("Novo Preço: ")
        if edicao == "V": lista[2] = input("Nova Validade: ")



def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Produto Excluido")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Código", chave)
        print("Dados", valor)

def finalizar():
    exit()