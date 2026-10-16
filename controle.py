# python3 controle.py
import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

def gerenciar_produtos():

    def adicionar_produto():

        while True:
            print ("---> Cadastrar um novo produto <---")

            id_ = input ("Digite o id: ")
            nome = input ("Digite o nome do produto: ")
            categoria = input ("Qual a categoria do produto? ")
            preco = float (input ("Qual o preço do produto? "))
            estoque = int (input ("Qual o estoque do produto? "))
            
            produtos.append({
                "id": id_,
                "nome": nome,
                "categoria": categoria,
                "preco": preco,
                "estoque": estoque
                })
            salvar_produtos(produtos)
            break
    def remover_produto():

        nome_produto = input ("Digite o nome do produto para remove-lo: ")

        for produto in carregar_produtos():
            if produto["nome"] == nome_produto:
                produtos.remove (produto)
                salvar_produtos(produtos)
                break    
    def adicionar_estoque():

        nome_produto = input ("Qual produto irá receber estoque? ")
        estoque = int (input ("Qual o novo estoque? "))
    
        for produto in carregar_produtos():       
            if produto["nome"] == nome_produto:
                produto["estoque"] = estoque
                salvar_produtos(produtos)

    while True:

        print (" ---> Menu <--- ")
        print ("1 - Adicinar produto")
        print ("2 - Remover produto")
        print ("3 - Adicionar estoque de um produto")
        print ("4 - Mostrar produtos com baixo estoque")
        print ("0 - Sair")


        opcao = input ("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            remover_produto()
        elif opcao == "3":
            adicionar_estoque()
        #elif opcao == "4":
            #mostrar_estoque()
        elif opcao == "0":
            print ("saindo do sistema...")
            break
        else:
            print ("æææææææææææ")

produtos = carregar_produtos()

while True:

    print (" ---> Menu <--- ")
    print ("1 - Carregar produtos")
    print ("2 - Salvar produtos")
    print ("3 - Mostrar produtos")
    print ("4 - Gerenciar produto")
    print ("0 - Sair")

    opcao = input ("Escolha uma opção: ")

    if opcao == "1":
        carregar_produtos()
    elif opcao == "2":
        salvar_produtos()
    elif opcao == "3":
        print (produtos)
    elif opcao == "4":
        gerenciar_produtos()
    elif opcao == "0":
        print ("saindo do sistema...")
        break
    else:
        print ("æææææææææææ")