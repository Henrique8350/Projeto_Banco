# Projeto_Banco

## 🌵 Cordel Bank 
Um simulador de gerenciamento de contas bancárias desenvolvido em Python.

O Cordel Bank é um simulador de banco, permitindo o cadastro de usuários, criação de contas, login e a realização de operações como depósito, saque, transferência, consulta de saldo e contratação de plano de crédito.
O projeto é modularizado.

## 🚀 Como Rodar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3.10+** instalado.

### Estrutura de Arquivos
O projeto utiliza uma estrutura modular, com as funções principais separadas em uma pasta `operacoes/`.

## ✨ Funcionalidades

O sistema permite as seguintes operações através de menus:

### Menu Inicial
* *Fazer Cadastro (1):* Cadastra um usuário com login, senha e código de verificação.
* *Fazer Login (2):* Autentica um usuário com login, senha e código de verificação.

### Menu de Operações
* **Criar Conta (1):** Cria uma conta bancária.
* *Depositar (2):* Deposita um valor no saldo da conta.
* *Sacar (3):* Retira um valor do saldo da conta.
* *Transferir (4):* Retira um valor do saldo e deposita no saldo de outra conta.
* *Consultar Saldo (5):* Exibe o saldo e o *Histórico* da conta.
* *Contratar Crédito (6):* Permite a contratação de plano de crédito baseado no saldo da conta.
* *Logout (7):* Encerra a sessão do usuário.
* *Sair (8):* Encerra o programa.

## 🛠️ Tecnologias Utilizadas

* *Python 3.10+*

### Requisitos funcionais (O que o sistema deve fazer):

1. Cadastro de usuário - O sistema deve permitir criar um novo usuário com login de até 10 caracteres e uma senha de 6 dígitos numéricos.
2. Login de usuário - O sistema deve autenticar o usuário através de login, senha e código de verificação.
3. Criação de conta bancária - O usuário logado deve poder criar uma conta bancária com saldo inicial e uma senha de  4 dígitos.
4. Gerar número da conta bancária - O sistema deve gerar um número de conta aleatório e único de 8 dígitos para cada conta.
5. Depósito - O sistema deve permitir adicionar um valor ao saldo de qualquer conta destino no sistema.
6. Saque - O sistema deve permitir sacar um valor da conta, desde que o valor seja menor ou igual ao saldo.
7. Transferência - O sistema deve permitir a transferência de um valor maior que 0 de uma conta origem à uma conta destino.
8. Consultar saldo - O usuário deve poder visualizar o saldo da conta.
9. Histórico -  O usuário deve poder visualizar o histórico de movimentações da conta.
10. Contratação de plano de crédito - O sistema deve permitir a contratação de um plano de crédito de até R$ 2.000,00
11. Logout - O sistema deve encerrar a sessão do usuário e retornar ao menu inicial.

### Requisitos não funcionais (Como o sistema deve se comportar):

1. Desempenho - O sistema apresenta um bom tempo de resposta.
2. Segurança - O sistema deve autenticar o usuário com as suas credenciais junto do código de verificação.
3. Usabilidade - O sistema apresenta facilidade de uso.
4. Confiabilidade - O sistema possui baixa frequência de falhas
5. Manutenibilidade - O sistema apresenta uma documentação clara.
6. Portabilidade - O sistema é compatível com o sistema operacional Windows.

Licenças Utilizadas

Esse Projeto está sob licença MIT
