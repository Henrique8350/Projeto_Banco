import time
from . import funcoes
import dados
import random

#Função para criar conta bancária
def criar_conta():
    print(f"\n~=====~= 1. CRIAR CONTA para {dados.USUARIO_LOGADO} ~=====~=")
            
    #Loop para que a senha da conta tenha 4 dígitos
    while True:
        try:
            senha_conta_str = int(input("Crie uma senha de 4 dígitos para operações: "))
            if len(str(senha_conta_str)) != 4:
                print("A senha deve ter 4 dígitos.")
            else:
                senha_conta = int(senha_conta_str)
                break
        except ValueError:
            print("Digite apenas números.")
            
    #Loop para que o saldo de seja maior ou igual a 0
    while True:
        try:
            saldo_inicial = float(input("Saldo inicial: "))
            if saldo_inicial < 0:
                print("Saldo menor que 0.")
            else:
                break
        except ValueError:
            print("Valor inválido.")

    #Loop para que o número da conta seja único
    while True:
        numero_conta = str(random.randint(10000000, 99999999))
        
        if not any(numero_conta in data['contas'] for data in dados.USUARIOS.values()):
            break
    
    #Guarda a conta no dicionário de contas do usuário
    dados.USUARIOS[dados.USUARIO_LOGADO]['contas'][numero_conta] = {
        'senha_conta': senha_conta,
        'saldo': saldo_inicial,
        'historico': [],
        'credito_contratado': False,
        'limite_credito': 0.0
    }
    
    print(f"\nConta bancária cadastrada.\nNúmero da conta: {numero_conta}")
    print(f"Saldo: R$ {saldo_inicial}")
    time.sleep(1)
