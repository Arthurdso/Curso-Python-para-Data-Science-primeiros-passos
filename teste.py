
# def saudacao():
#     nome = input('Qual o seu nome? ')
#     print(f'Olá {nome}')

# saudacao();

# def saudacao_com_parametro(nome_da_pessoa):
#     print(f'olá {nome_da_pessoa}')
    
# saudacao_com_parametro('Arthur');

# idade = 10;

# FUNCAO COM PARAMETROS
# def verifica_se_pode_dirigir(idade):
#     if idade >=18:
#         print('Tem Permissao para dirigir')
#     else:
#         print('Não tem permissao para dirigir')
        
# verifica_se_pode_dirigir(idade)

# Função sem parametros
def verifica_se_pode_dirigir_sem_parametro():
    idade = int(input('Qual sua idade ? '))
    if idade >= 18:
        print('Tem Permissao')
    else:
        print('Não tem permissao');
        
verifica_se_pode_dirigir_sem_parametro();