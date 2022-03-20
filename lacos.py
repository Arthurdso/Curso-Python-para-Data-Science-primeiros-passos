
idades = [18, 22, 15, 50, 12, 13, 40]

# def verifica_se_pode_dirigir(idade):
#     if idade >= 18:
#         print(f'{idade} anos de idade, TEM permissao para dirigir')
#     else:
#         print(f'{idade} anos de idade, NÃO tem permissao para dirigir')


# for fora da funcao
# for idade in idades:
#     verifica_se_pode_dirigir(idade)

# for dentro da funcao
def verifica_se_pode_dirigir(idades):
    for idade in idades:
        if idade >= 18:
            print(f'{idade} anos de idade, TEM permissao para dirigir')
        else:
            print(f'{idade} anos de idade, NÃO tem permissao para dirigir')


verifica_se_pode_dirigir(idades)
