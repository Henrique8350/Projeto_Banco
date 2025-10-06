import time
from . import funcoes
import dados

#Função para transferir
def transferir():
    if not dados.USUARIO_LOGADO: 
        return
    
    print("\n~=====~= 4. TRANSFERIR ~=====~=")
    
    numero_origem = input("Digite o número da sua conta: ").strip()
    senha = input("Senha de operações: ").strip()
    
    #Verifica se a conta e a senha existem no dicionário do usuário
    conta_origem = funcoes.selecionar_conta_usuario(numero_origem, senha)
    if not conta_origem: return
    
    #Verifica se a conta destino existe no dicionário
    numero_destino = input("Digite a conta de destino: ").strip()
    conta_destino = funcoes.encontrar_conta_usuario(numero_destino)
            
    if not conta_destino:
        print("Conta destino não existe.")
        time.sleep(1)
        return

    if numero_origem == numero_destino:
        print("Não é possível transferir para a mesma conta.")
        time.sleep(1)
        return
        
    while True:
        try:
            valor = float(input("Valor da Transferência: "))
            if valor <= 0:
                print("Valor deve ser maior que zero.")
            elif valor > conta_origem['saldo']:
                print(f"Saldo insuficiente.\n Saldo: R$ {conta_origem['saldo']}")
                time.sleep(1)
                return
            else:
                break
        except ValueError:
            print("Valor inválido.")

    #Subtração do valor da conta origem
    conta_origem['saldo'] -= valor
    #Adição do valor na conta destino
    conta_destino['saldo'] += valor
    
    #Registra a transferência no histórico das contas origem e conta destino
    funcoes.registrar_historico(conta_origem, "TRANSFERENCIA", valor, numero_destino)
    funcoes.registrar_historico(conta_destino, "RECEBIMENTO", valor, numero_origem)
    
    print("\nTransferência realizada")
    print(f"Saldo atualizado: R$ {conta_origem['saldo']}")
    time.sleep(2)
