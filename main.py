from Funcoes.funcoes import*

usuarios={}

opcao=perguntar()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="X" or opcao=="L" or opcao=="F":
    if opcao=="I":
        inserir(usuarios)

    if opcao=="P":
        pesquisar(usuarios, input("Qual o Código que deseja pesquisar?"))

    if opcao=="E":
        editar(usuarios,  input("Código do produto a ser alterado?"))

    if opcao=="X":
        excluir(usuarios, input("Qual login deseja excluir?"))

    if opcao=="L":
        listar(usuarios)
    opcao = perguntar()

    if opcao=="F":
        finalizar()
