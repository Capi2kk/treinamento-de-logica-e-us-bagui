#NAO SEI MAIS OQE FAZER ENTAO VOU COLOCAR QUALQUER COISA AQUI QUE ENVOLVA FUNÇAOS
#tive a ideia (chatgpt que deu kkkkkk) de fazer tipo uma lojinha online simples com funçus 
#vou farmar aura, e o recai nao pode saber disso
#essa merda vai ser assutadoramente grande pois estou com ideias demais
import time
import os
import sys
import random

produtos = {}

def produtos_disponiveis():
    print("produtos disponiveis para venda:")
    if produtos == {}:
        print("Nenhum produto cadastrado.")

    elif produtos != {}:
        for produto, detalhes in produtos.items():
            print(f"Produto: {produto}, Preço: R${detalhes['preco']}, Estoque: {detalhes['estoque']}")

    else:
        print("Erro ao listar produtos.")

def cadastrar_produto():
    nome = input("digite o nome do do produto:")
    preço = float(input("digite o preço do produto:"))
    estoque = int(input("digite a quantidade em estoque:"))
    produtos[nome] = {'preco': preço, 'estoque': estoque}
    carregando_produtos()
    print(f"Produto {nome} cadastrado com sucesso!")
    time.sleep(1)

def comprar_produto():
    produtos_disponiveis()
    nome = input("digite o nome do produto que deseja comprar:")
    if nome in produtos:
        quantidade = int(input("digite a quantidade que deseja comprar:"))
        if quantidade <= produtos[nome]['estoque']:
            total = produtos[nome]['preco'] * quantidade
            produtos[nome]['estoque'] -= quantidade
            carregando_produtos()
            print(f"Compra realizada com sucesso! Total: R${total}")
        else:
            print("Quantidade em estoque insuficiente.")

    else:
        print("Produto não encontrado.")
    time.sleep(1)

def limpar():  #funcao para limpar a tela
    if os.name == "nt":
        os.system("cls")

def carregando_produtos(): #animaçaão muito foda de carregamentos
    espera = random.randint(1, 7)
    duracao = espera
    progresso = 0
    print(f"Carregando produtos no banco de dados... Tempo estimado: {espera}s")
    inicio = time.time()
    while progresso < 100:
        tempo_passado = time.time() - inicio
        progresso = min(int((tempo_passado / duracao) * 100), 100)
        barra = "#" * (progresso // 5) + "-" * (20 - (progresso // 5))
        print(f"\r[{barra}] {progresso}%", end="")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\nProdutos carregados com sucesso!")


def menu():
    while True:
        print("\n=== loja do capi2kk ===")
        print("1. cadastrar Produto")
        print("2. comprar Produto")
        print("3. listar Produtos Disponíveis")
        print("4. sair")
        escolha = input("escolha uma opção:")
        
        if escolha == '1':
            cadastrar_produto()
        elif escolha == '2':
            comprar_produto()
        elif escolha == '3':
            produtos_disponiveis()
            time.sleep(2)
        elif escolha == '4':
            print("Fechando sistema", end="")
            for _ in range(6): #vai fazer uma animaçao muito foda 😭🔥🔥
                for i in range(3):
                    time.sleep(0.3)
                    print(".", end="")
                    sys.stdout.flush()
                time.sleep(0.3)
                print("\b\b\b   \b\b\b", end="")
            print("\nSistema fechado com sucesso! Ate a proxima!") 
            time.sleep(1.5)
            limpar()
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)

menu()

