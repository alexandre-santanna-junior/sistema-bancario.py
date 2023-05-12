saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
limite_de_saques = 3

#==============================================================================

def realizar_deposito(saldo, extrato):
    valor_do_deposito = float(input('Iforme o valor do depósito:'))
    if valor_do_deposito > 0:
        saldo += valor_do_deposito
        extrato += f'Depósito de {valor_do_deposito}\n'
    else:
        print('A operação falhou. O valor informado é inválido.')
    return saldo, extrato

#==============================================================================

def realizar_saque(saldo, extrato, numero_de_saques, limite_de_saques, limite):
    valor_saque = float(input('Informe o valor do saque:'))
    numero_de_saques += 1
    saldo -= valor_saque
    extrato += f'Saque de {valor_saque:.2f}\n'
    
    if valor_saque > limite:
        print('Operação falhou. O valor do saque excede o limite.')
    elif valor_saque <= 0:
        print('A operação falhou. O valor informado é inválido.')
    elif valor_saque > saldo:
        print('Operação falhou, você não possui saldo suficiente.')
    elif numero_de_saques > limite_de_saques:
        print('Operação falhou, você ja fez os três saques diários.')
    return saldo, extrato, numero_de_saques
        
#==============================================================================

def mostrar_extrato(saldo, extrato):
    print('==========EXTRATO==========\n')
    print('Saldo:{:.2f}\n'.format(saldo))
    print(extrato)
    print('===========================')
    

    