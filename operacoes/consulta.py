import time 
from . import funcoes
import dados

#Função para consultar saldo
def consultar_saldo():
    if not dados.USUARIO_LOGADO: 
        return
    
    print("\n~=====~= 5. CONSULTAR SALDO ~=====~=")
    
    numero_conta = input("Número da Sua Conta: ").strip()
    senha = input("Senha de Operações (4 dígitos): ").strip()
    
    #Verifica a conta e a senha cadastrados
    conta = funcoes.selecionar_conta_usuario(numero_conta, senha)
    
    if conta:
        print(f"\n--- INFORMAÇÕES DA CONTA {numero_conta} ---")
        print(f"Saldo: R$ {conta['saldo']}")
        #Se o usuário contratou o plano de crédito, mostra o limite
        if conta['credito_contratado']:
            print(f"Limite Disponível: R$ {conta['limite_credito']}")

        print("\n~=====~= Histórico de Transações ~=====~=")
        historico = conta['historico']
        
        if not historico:
            print("Nenhuma movimentação.")
        else:
            for i in historico: 
                print(i)
