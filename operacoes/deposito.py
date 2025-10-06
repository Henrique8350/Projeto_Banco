import time
from . import funcoes
import dados

#Função para depositar
def depositar():
    if not dados.USUARIO_LOGADO: 
        return
    
    print("\n~=====~= 2. DEPOSITAR ~=====~=")
    
    numero_conta = input("Digite o número da conta destino: ").strip()
    conta_destino = funcoes.encontrar_conta_usuario(numero_conta)
    
    #Verifica se a conta destino existe no dicionário
    if not conta_destino:
        print("Conta destino não existe.")
        time.sleep(1)
        return
        
    while True:
        try:
            valor = float(input("Valor do Depósito: "))
            if valor <= 0:
                print("Valor deve ser maior que 0.")
            else:
                break
        except ValueError:
            print("Valor inválido.")

    #Adiciona o valor ao saldo da conta destino.
    conta_destino['saldo'] += valor
    
    #Registra o depósito no histórico da conta destino.
    funcoes.registrar_historico(conta_destino, "DEPOSITO", valor)
    
    print("\nDepósito realizado.")
    print(f"Saldo atualizado: R$ {conta_destino['saldo']}")
    time.sleep(2)
