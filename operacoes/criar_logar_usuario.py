import time
import random
import dados
from . import funcoes

#Função para cadastrar novo usuário
def criar_usuario():
    print("\n~=====~= 1. TELA DE CADASTRO ~=====~=")
    
    #Loop para o login ter no máximo 10 caracteres.
    while True:
        login_nome = input("Crie um login (até 10 letras): ").strip()
        if len(login_nome) > 10:
            print("Login deve ter no máximo 10 caracteres.")
        else:
            break
    
    #Loop para a senha ter 6 dígitos.      
    while True:
        try:
            senha = int(input("Crie uma senha de 6 dígitos numéricos: "))
            if len(str(senha)) != 6:
                print("A senha deve ter 6 dígitos numéricos.")
            else:
                break
        except ValueError:
            print("Digite apenas números.")

    codigo_ver = random.randint(1000, 9999)
    
    dados.USUARIOS[login_nome] = {
        'senha_login': senha,
        'codigo_verificacao': codigo_ver,
        'contas': {}
    }
    
    print("\nCadastro realizado")
    print(f"Seu código de verificação é: {codigo_ver}.")
    time.sleep(2)
    return login_nome

#Função de login
def login_usuario():
    print("\n~=====~= 2. TELA DE LOGIN ~=====~=")
    
    login = input("Digite seu login: ").strip()
    
    #Verifica se o login existe no dicionário de usuários
    if login in dados.USUARIOS:
        usuario_info = dados.USUARIOS[login]
        
        try:
            senha = int(input("Digite sua senha de 6 dígitos: "))
        except ValueError:
            print("Senha inválida.")
            time.sleep(1)
            return False

        #Compara a senha digita com que está cadastrada
        if usuario_info['senha_login'] == senha:
            codigo_digitado = input("Digite o código de verificação: ")
            
            if str(usuario_info['codigo_verificacao']) == codigo_digitado:
                #Importa o usuário para a constante global USUARIO_LOGADO
                dados.logar_usuario(login)
                print(f"\nBem-vindo(a), {login}!")
                time.sleep(1)
                return True
            else:
                print("Código de verificação incorreto.")
        else:
            print("Senha incorreta.")
    else:
        print("Login não encontrado.")
    
    #Caso retorne false, a constante USUARIO_LOGADO fica none
    dados.logar_usuario(None)
    time.sleep(2)
    return False
