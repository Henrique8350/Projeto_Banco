import time
from . import funcoes
import dados

#Função para calcular o limite de crédito

def calcular_limite(saldo):
    limite_credito = 0.0
    if saldo < 500.00:
        limite_credito = 0.0
    elif saldo <= 1000.00:
        limite_credito = 500.00
    else:
       limite_credito = 2000.00
    
    return limite_credito

#Função para contratar o plano de crédito
def contratar_credito():
    if not dados.USUARIO_LOGADO: 
        return
    
    print("\n~=====~= 6. CONTRATAR CRÉDITO ~=====~=")
    
    numero_conta = input("Digite o número da sua conta: ").strip()
    senha = input("Senha de operações): ").strip()
    
    #Verifica se a conta e a senha existem no dicionário
    conta = funcoes.selecionar_conta_usuario(numero_conta, senha)
    if not conta: return

    limite_credito = calcular_limite(conta['saldo'])
    
    if not conta['credito_contratado']:
        if saldo < 500.00:
            print("Seu saldo deve ser maior ou igual a R$ 500,00 para contratar o plano de crédito.")
            time.sleep(2)
            return

        print(f"Seu limite é R$ {limite_credito}")
        print(f"Digite 's' para Sim ou 'n' para Não.")
        escolha = input("Deseja contratar o plano de crédito com este limite? ").lower()
        
        if escolha == 's':
            conta['credito_contratado'] = True
            conta['limite_credito'] = limite_credito
            funcoes.registrar_historico(conta, "PLANO CREDITO", limite_credito)
            print("\nContratação realizada")
        else:
            print("Contratação cancelada.")
    time.sleep(2)
