#primeira vez q tive uma ideia propria, fazer sla, qualquer porra com login  chaves e essa porra ai
#jojos amo ARARARARAA ORARAROOARORAO
#vai estar cheio de bugs
#foda-se
#vou melhorar com o tempo


import random
import string
import time 
import sys


chaves = {}

#------------baguio de logins-------------

def gerar_chave():
    chave_enter = input("Digite a chave a qual deseja criar: ")
    time.sleep(0.2)
    if chave_enter in chaves:
        print("erro: chave ja existente")
        return
    time.sleep(0.2)
    if chave_enter in string.punctuation or ' ' in chave_enter:
        print("erro: chave invalida")
        return
    time.sleep(1)
    decodfic = input("Digite o codigo de decodificacao para essa chave (deve conter 8 caracteres): ")
    time.sleep(1)
    chaves[chave_enter] = decodfic
    print(f"Chave '{chave_enter}' criada com sucesso!")
    time.sleep(0.4)
    print(f"Codigo de decodificacao: {decodfic}")

def ver_chaves():
    if not chaves:
        print("\nNenhuma chave criada ainda.")
        return

    time.sleep(1)

    print("\n----------------------------------------")
    print("           Chaves Criadas")
    print("----------------------------------------\n")

    print("Chaves criadas:\n")

    for chave, codigo in chaves.items():
        print(f" - Chave: {chave} | Codigo de decodificacao: {codigo}")

    print("\n----------------------------------------\n")


def limpar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def sair():
            print("Fechando sistema", end="")
            for _ in range(6): #vai fazer uma animaçao muito foda 😭🔥🔥
                for i in range(3):
                    time.sleep(0.3)
                    print(".", end="")
                    sys.stdout.flush()
                time.sleep(0.3)
                print("\b\b\b   \b\b\b", end="")
            print("\nSistema fechado com sucesso! Ate a proxima!") 
            time.sleep(0.5)
            limpar()
            sys.exit()

            

def carregando(): #animaçaão muito foda de carregamentos copiada do treino3_logica.py
    espera = random.randint(1, 4)
    duracao = espera
    progresso = 0
    print(f"Conferindo no banco de dados... Tempo estimado: {espera}s")
    inicio = time.time()
    while progresso < 100:
        tempo_passado = time.time() - inicio
        progresso = min(int((tempo_passado / duracao) * 100), 100)
        barra = "#" * (progresso // 5) + "-" * (20 - (progresso // 5))
        print(f"\r[{barra}] {progresso}% ", end="")
        sys.stdout.flush()
        time.sleep(0.1)



def menu_login():
    while True:
        print("Bem-vindo ao menu de logins.")
        print("1. Gerar nova chave")
        print("2. Ver chaves criadas")
        print("3. Sair")
        escolha = input("Escolha uma opcao (1-3): ")
        
        if escolha == '1':
            gerar_chave()
        elif escolha == '2':
            ver_chaves()
        elif escolha == '3':
            sair()
        else:
            print("Opcao invalida, tente novamente.")
        print("\n")

#---------------------menu pricipal---------------------

def login():
    login_user = input("Digite sua chave de login: ")
    login_user_cod = input("Digite seu codigo de decodificacao: ")
    carregando()
    if login_user in chaves and str(chaves[login_user]) == login_user_cod:
        print("login bem sucedido!")

        menu_logado_user()
        time.sleep(1)
        limpar()
        menu_login()
    else:
        print("Login falhou: chave ou codigo incorretos.")
        time.sleep(1)
        limpar()
        

def menu_logado_user():
    while True:
        menu_login_user = input(
"""=== Menu do Usuario ===
1 Ver chaves criadas
2 ver banco
3 painel admin
4 ver produtos
5 sair
Escolha uma opcao (1-5): """
        )

        if menu_login_user == '1':
            ver_chaves()

        elif menu_login_user == '2':
            banco()

        elif menu_login_user == '3':
            painel_admin()

        elif menu_login_user == '4':
            ver_produtos()

        elif menu_login_user == '5':
            sair()



def banco():
    print("Banco ainda não implementado.")
    menu_logado_user()

def painel_admin():
    painel_admin_pass = input("Digite a senha do painel admin: ")
    if painel_admin_pass == "ui123":
        print("Acesso ao painel admin concedido.")
        painel_admin_menu()
    else:
        print("Senha incorreta. Acesso negado.")
        menu_logado_user()

def painel_admin_menu():
    while True:
        adimim_menu = input("""=== Painel Admin ===
                            1 Ver chaves criadas
                            2 Tirar chave
                            3 Banir chaves
                            4 mudar senha do painel admin
                            5 Voltar ao menu do usuario
                            Escolha uma opcao (1-5): """)
        if adimim_menu == '1':
            ver_chaves()
        elif adimim_menu == '2':
            tirar_chave()
        elif adimim_menu == '3':
            banir_chave()
        elif adimim_menu == '4':
            mudar_senha_admin()
        elif adimim_menu == '5':
            menu_logado_user()

def tirar_chave():
    chave_tirar = input("Digite a chave que deseja tirar: ")
    ver_chaves()
    if chave_tirar in chaves:
        del chaves[chave_tirar]
        print(f"Chave '{chave_tirar}' removida com sucesso.")
    else:
        print("Chave nao encontrada.")
    menu_logado_user()
    painel_admin_menu()

def banir_chave():
    banir_chave_input = input("Digite a chave que deseja banir: ")
    if banir_chave_input in chaves:
        del chaves[banir_chave_input]
        print(f"Chave '{banir_chave_input}' banida com sucesso.")
    else:
        print("Chave nao encontrada.")
    painel_admin_menu()

def mudar_senha_admin():
    nova_senha = input("Digite a nova senha do painel admin: ")
    global painel_admin_pass
    painel_admin_pass = nova_senha
    print("Senha do painel admin alterada com sucesso.")
    painel_admin_menu()

def ver_produtos():
    print("Produtos ainda não implementado.")
    menu_logado_user()

    
def menu_pricipal():
    while True:
        menu_pricipal_pergunta = input (f"=== Bem vindo ao NextCoi - Menu ==="
                                        "\n1 Fazer login"
                                        "\n2 Criar nova chave"
                                        "\n3 Sair"
                                        "\nEscolha uma opcao (1-2): ")
        
        if menu_pricipal_pergunta == '1':
            login()
        elif menu_pricipal_pergunta == '2':
            gerar_chave()
        elif menu_pricipal_pergunta == '3':
            sair()
        else:
            print("Opcao invalida, tente novamente.")
            time.sleep(1)
            limpar()


menu_pricipal()





    
