import time
from . import funcoes
import dados

#Funcão para sacar
def sacar():
    if not dados.USUARIO_LOGADO: 
        return
    
    print("\n~=====~= 3. SACAR ~=====~=")
    
    numero_conta = input("Digite o número da sua conta: ").strip()
    senha = input("Digite a sua senha de operações: ").strip()
    
    #Verifica se a conta e a senha existem no dicionário
    conta = funcoes.selecionar_conta_usuario(numero_conta, senha)
    if not conta: return

    #Loop para que o valor do saque seja maior ou igual a 0 e menor ou igual ao saldo
    while True:
        try:
            valor = float(input("Digite o valor que deseja sacar: "))
            if valor <= 0:
                print("Valor deve ser maior que 0.")
                time.sleep(1)
                return
            if valor > conta['saldo']:
                print("O saque desejado é maior que o saldo.")
                time.sleep(1)
                return
            break
        except ValueError:
            print("Valor inválido.")

    #Cálculo do saque
    if conta['saldo'] >= valor:
        conta['saldo'] -= valor
        funcoes.registrar_historico(conta, "SAQUE", valor)
        print("\nSaque realizado")
    else:
        print("Saldo insuficiente.")

    print(f"Saldo atualizado: R$ {conta['saldo']}")
    time.sleep(2)
