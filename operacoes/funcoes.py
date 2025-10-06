from datetime import datetime
import time
import dados

#Função para registrar o histório do usuário
def registrar_historico(conta_info, tipo, valor, destino=None):
    data_hora = datetime.now().strftime("%d/%m %H:%M")
    
    historico = f"{data_hora} | {tipo}: R$ {valor}"
    
    if destino:
        historico += destino
    
    #Adiciona a movimentação na lista de histórioco da conta.
    conta_info['historico'].append(historico)

#Função que verifics se a conta e a senha existem no dicionário do usuário
def selecionar_conta_usuario(numero_conta, senha_conta_str):
    #Verifica se o usuário está logado, verificando se o login_nome existe na constante USUARIO_LOGADO
    if dados.USUARIO_LOGADO not in dados.USUARIOS:
        print("Você precisa estar logado.")
        return None
        
    #Busca as contas cadastradas no dicionário 'contas' do usuário
    contas_do_usuario = dados.USUARIOS[dados.USUARIO_LOGADO]['contas']
    
    if numero_conta in contas_do_usuario:
        conta_info = contas_do_usuario[numero_conta]
        
        try:
            #Converte a senha digitada para números
            senha_conta_int = int(senha_conta_str)
        except ValueError:
            print("A senha de operações deve ser em números.")
            return None

        #Se a senha estiver correta, retorna as informações da conta
        if conta_info['senha_conta'] == senha_conta_int:
            return conta_info
        else:
            print("Senha errada")
            time.sleep(1)
    else:
        print("Conta não encontrada.")
        time.sleep(1)
    return None

#Função para buscar a conta em no dicionário de usuários
def encontrar_conta_usuario(numero_conta):
    for dados_usuarios in dados.USUARIOS.values():
        if numero_conta in dados_usuarios['contas']:
            return dados_usuarios['contas'][numero_conta]
    #Retorna none se não encontrar a conta
    return None
