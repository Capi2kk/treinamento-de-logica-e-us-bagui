#nesse treino meu vamos criar uma ideia do chatgpt, um banco que usado comandos
import os
import time
import sys

def limpar():  #funcao para limpar a tela
    if os.name == "nt":
        os.system("cls")

usuario_dicionario = {} 

usuario_resposta =input("Bem-vindo ao banco, Qual seu usuario?:")

if usuario_resposta in usuario_dicionario:
    print("Bem-vindo de volta", usuario_resposta)
else:
    print("usuario nao encontrado, criando novo usuario...")
    usuario_dicionario[usuario_resposta] = {"saldo": 0}


print("Bem-vindo ao banco.", usuario_resposta+" seu saldo atual e de: R$", usuario_dicionario[usuario_resposta]["saldo"])
while True:
    resposta = input("Oque voce desaja fazer hoje?: (1) sacar, (2) emprestimo , ou (3) sair?")

    if resposta == "1":
        valor_saque = int(input("Quanto voce deseja sacar?: R$"))
        if valor_saque > usuario_dicionario[usuario_resposta]["saldo"]:
            print("Saldo insuficiente para saque.")
            print("Sem dinheiro? Que tal um emprestimo? Clique na tecla 2 para solicitar um emprestimo!")
        
        else:
            valor_saque < usuario_dicionario[usuario_resposta]["saldo"]
            usuario_dicionario[usuario_resposta]["saldo"] -= valor_saque
            print("Saque de R$", valor_saque, "realizado com sucesso, agora seu saldo e de: R$", usuario_dicionario[usuario_resposta]["saldo"] )
    elif resposta == "2":
        valor_emprestimo = int(input("Quanto voce deseja de emprestimo?: R$"))
        usuario_dicionario[usuario_resposta]["saldo"] += valor_emprestimo
        print("Emprestimo de R$", valor_emprestimo, "concedido com sucesso, agora seu saldo e de: R$", usuario_dicionario[usuario_resposta]["saldo"] )
    
    elif resposta == "3":
        print("Obrigado por usar nosso banco, ate mais!")
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



