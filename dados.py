#Dicionário para guardar todos os usuários
USUARIOS = {}

#Constante para guardar o login do usuário
USUARIO_LOGADO = None

#Função para logar usuario
def logar_usuario(login_nome):
    global USUARIO_LOGADO
    USUARIO_LOGADO = login_nome
