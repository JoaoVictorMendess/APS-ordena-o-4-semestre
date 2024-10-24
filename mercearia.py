import os
import csv

def cadastrar_produto():
        os.system("cls")
        print("\tCADASTRO DE PRODUTOS\n\n")
        nome = (input("\t\tInforme o nome do produto: "))
        descricao = (input("\t\tInforme a descrição do produto: "))
        while True:
            try:
                qtd = int(input("\t\tInforme a quantidade de produtos: "))
                break
            except ValueError:
                print("\t\tInforme um número válido")
        categoria = (input("\t\tInforme a categoria do produto: "))
        while True:
            try:
                preco = float(input("\t\tInforme o preço do produto: "))
                break
            except ValueError:
                print("\t\tInforme um número válido")
        
        arquivo = open(CSV_FILE, mode='a', newline='')
        linha = f"{nome};{descricao};{qtd};{categoria};{preco}\n"
        arquivo.write(linha)
        arquivo.close
        print("Registro realizado com sucesso")
        
def listar_produtos():
    os.system("cls")
    print("\tPRODUTOS DISPONÍVEIS\n\n")
    arquivo = open(CSV_FILE, mode="r")
    linhas = arquivo.readlines()
    if len(linhas) == 0:
        print("Nenhum produto cadastrado.")
    else:
        print(f"{'Nome'} {'Descrição'} {'Qtd'} {'Categoria':} {'Preço'}")
        for linha in linhas:
            print(linha)
    arquivo.close
    
def deletar_produto():
    os.system("cls")
    listar_produtos()
    nome_do_produto = input("\nDigite o nome do produto que deseja deletar: ")
    
    arquivo = open(CSV_FILE, mode="r")
    linhas = arquivo.readlines()
    arquivo.close()
        
    arquivo = open(CSV_FILE, mode="w")
    for linha in linhas:
        if not linha.startswith(nome_do_produto):
            arquivo.write(linha)
    arquivo.close() 
    print(f"Produto '{nome_do_produto}' deletado com sucesso!")
        

def atualiza_produto():
    os.system("cls")
    listar_produtos()
    nome_produto = input("\nDigite o nome do produto que deseja atualizar: ")
    
    arquivo = open(CSV_FILE, mode="r")
    linhas = arquivo.readlines()
    arquivo.close()
    
    produto_encontrado = False
    linhas_novas = []
    
    for linha in linhas:
        if linha.startswith(nome_produto):
            produto_encontrado = True
            print("\nProduto encontrado! Informe os novos dados:")
            nome = input("\t\tNovo nome: ")
            descricao = input("\t\tNova descrição: ")
            while True:
                try:
                    qtd = int(input("\t\tNova quantidade: "))
                    break
                except ValueError:
                    print("\t\tInforme um número válido")
            categoria = input("\t\tNova categoria: ")
            while True:
                try:
                    preco = float(input("\t\tNovo preço: "))
                    break
                except ValueError:
                    print("\t\tInforme um número válido")
            linha_nova = f"{nome};{descricao};{qtd};{categoria};{preco}\n"
            linhas_novas.append(linha_nova)
        else:
            linhas_novas.append(linha)
            
    if produto_encontrado:
        arquivo = open(CSV_FILE, mode="w", newline='')
        arquivo.writelines(linhas_novas)
        arquivo.close()
    else:
        print(f"Produto '{nome_produto}' não encontrado.")

CSV_FILE = 'produtos.csv'
opcao = 0
while opcao != 5:
    os.system("cls")
    print("\tSISTEMA DE MERCEARIA\n\n")
    print("\t1. Cadastrar produtos")
    print("\t2. Atualizar produto")
    print("\t3. Listar Produtos")
    print("\t4. Deletar Produto")
    print("\t5. Sair")
    while True:
        try:
            opcao = int(input("\t\tDigite a opção desejada: "))
            break
        except ValueError:
            print("Opção inválida. Por favor, insira um número.")

    # opcao = int(input("\t\tDigite a opção desejada: "))
    
    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        atualiza_produto()
    elif opcao == 3:
        listar_produtos()
    elif opcao == 4:
        deletar_produto()
    elif opcao == 5:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
    
    input("\nPressione ENTER para continuar...")
    
    