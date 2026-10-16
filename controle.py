# python3 controle.py
import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=false)
    arquivos.close()


while True:

    print (" ---> Menu <--- ")
    print ("1 - carregar produtos")
    print ("2 - salvar produtos")
    print ("0 - Sair")

    opcao = input ("Escolha uma opção: ")

    if opcao == "1":
        carregar_produtos()
    elif opcao == "2":
        salvar_produtos()
    elif opcao == "0":
        print ("saindo do sistema...")
        break
    else:
        print ("æææææææææææ")