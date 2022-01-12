import re

def valida_cnpj(cnpj):
    cnpj = valida_numero(cnpj)
    validar = gerador_novo_cnpj(cnpj)
    if validar == cnpj:
        return f'O CNPJ {cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]} É valido!'
    else:
        return f'O CNPJ {cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]} NÃO É valido!'

def remover_caracteres(cnpj_sem_caracters):
    return re.sub(r'[^0-9]','',cnpj_sem_caracters)

def valida_numero(valida_numero_cnpj):
    numero_validado = remover_caracteres(valida_numero_cnpj)
    while len(numero_validado) != 14 or numero_validado == numero_validado[::-1]:
        numero_validado = input('CNPJ inválido!\nDigite um CNPJ de 14 caracteres: ')
        numero_validado = remover_caracteres(numero_validado)
    return numero_validado

#  Gera um novo CNPJ a partir do CNPJ que o usuário digitou
def gerador_novo_cnpj(novo_cnpj):

    valida_parte1 = novo_cnpj[0:5]
    valida_parte2 = novo_cnpj[4:12]
    soma = 0

    for i, v in enumerate(range(5,1,-1)):
        multiplicador = v * int(valida_parte1[i])
        soma += multiplicador

    for i, v in enumerate(range(9, 1, -1)):
        multiplicador = v * int(valida_parte2[i])
        soma += multiplicador

    digito = 11 - (soma % 11)

    if digito > 9:
        novo_cnpj = novo_cnpj[0:12] + '0'
    else:
        novo_cnpj = novo_cnpj[0:12] + str(digito)

    valida_parte1 = novo_cnpj[0:6]
    valida_parte2 = novo_cnpj[5:13]
    soma = 0

    for i, v in enumerate(range(6, 1, -1)):
        multiplicador = v * int(valida_parte1[i])
        soma += multiplicador

    for i, v in enumerate(range(9, 1, -1)):
        multiplicador = v * int(valida_parte2[i])
        soma += multiplicador

    digito = 11 - (soma % 11)

    if digito > 9:
        novo_cnpj = novo_cnpj[0:13] + '0'
    else:
        novo_cnpj = novo_cnpj[0:13] + str(digito)

    return novo_cnpj

