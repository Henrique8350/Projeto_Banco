import time
import dados

from operacoes.criar_logar_usuario import criar_usuario, login_usuario
from operacoes.cadastrar_conta import criar_conta
from operacoes.deposito import depositar
from operacoes.saque import sacar
from operacoes.transferencia import transferir
from operacoes.consulta import consultar_saldo
from operacoes.credito import contratar_credito

# Menu da tela inicial
def main_loop():
    
    print("\nOlá, seja bem vindo ao Cordel Bank, sua melhor escolha de banco no nordeste!")
    time.sleep(1)
    
    while True:
        print("\n~=~=~=~=~=~~= Menu - Cordel Bank ~=~=~=~=~=~~=")
        print("\n1 - Fazer Cadastro")
        print("2 - Fazer Login")
        print("3 - Sair do Programa")

        try:
            escolha = int(input("\nO que deseja fazer? (1, 2 ou 3): "))
        except ValueError:
            print("Digite um número.")
            time.sleep(1)
            continue
            
        match escolha:
            case 1:
                criar_usuario()
            case 2:
                if login_usuario():
                    if not menu_operacoes():
                        break
            case 3:
                print("Obrigado por usar o Cordel Bank.")
                time.sleep(2)
                break 
            case _:
                print("Opção inválida.")
                time.sleep(1)

# Menu de operações
def menu_operacoes():
    
    opcoes_menu = [
        "1 - Criar Conta",
        "2 - Depositar",
        "3 - Sacar",
        "4 - Transferir",
        "5 - Consultar Saldo",
        "6 - Contratar Crédito",
        "7 - Logout e Voltar",
        "8 - Sair do Sistema"
    ]
    
    funcoes_menu = {
        1: criar_conta,
        2: depositar,
        3: sacar,
        4: transferir,
        5: consultar_saldo,
        6: contratar_credito
    }

    while True:
        print(f"\nMENU - {dados.USUARIO_LOGADO}")
        for i in opcoes_menu:
            print(i)

        try:
            escolha = int(input("\nEscolha a opção (1-8): "))
        except ValueError:
            print("\nDigite um número.")
            time.sleep(1)
            continue

        match escolha:
            case 1 | 2 | 3 | 4 | 5 | 6:
                funcoes_menu[escolha]()
            case 7:
                print("\nLogout...")
                dados.logar_usuario(None)
                time.sleep(1)
                return True
            case 8:
                print("\nSaindo do sistema...")
                time.sleep(2)
                return False
            case _:
                print("\nOpção inválida.")
                time.sleep(1)

main_loop()
