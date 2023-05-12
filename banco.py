from funcoes import realizar_deposito, realizar_saque, mostrar_extrato

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
limite_de_saques = 3
conta = 0
usuarios = [{'nome': 'Alexandre Santanna Junior', 'data de nascimento': '2001', 'CPF': '37524467818', 'conta': '0001'}]
numero_de_contas = 1

while True:
    print("""
    [e] ENTRAR 
    [c] SE CADASTRAR
    [s] SAIR DO SISTEMA
    """)
    acessar = input('DIGITE A OPÇÃO QUE VOCÊ DESEJA:').upper()
    if acessar == 'E':
        informar_cpf = input('Informe seu CPF: ')
        for usuario in usuarios:
            if usuario['CPF'] == informar_cpf:
                print('Seja bem-vindo, {} | conta {}'.format(usuario['nome'],usuario['conta']))
                print("""
                [1] DEPÓSITO
                [2] SAQUE 
                [3] EXTRATO 
                [4] ENCERRAR MOVIMENTAÇÃO BANCÁRIA
                """)

                while True:
                    menu = int(input('DIGITE A OPÇÃO QUE VOCÊ DESEJA: '))
                    if menu == 1:
                        saldo, extrato = realizar_deposito(saldo, extrato)
                    elif menu == 2:
                        saldo, extrato, numero_de_saques = realizar_saque(saldo, extrato, numero_de_saques, limite_de_saques, limite)
                    elif menu == 3:
                        mostrar_extrato(saldo, extrato)
                    elif menu == 4:
                        print('Obrigado por usar nossos serviços, {}!'.format(usuario['nome']))
                        break
                    else:
                        print('Opção inválida!')

                print('Banco do Brasil')
                break
        else:
            print('Você não possui cadastro. Por favor, volte para a tela inicial e faça seu cadastro.')
    elif acessar == 'C':
        print('Informe seus dados para efetuar o cadastro:')
        cadastro_nome = input('Nome: ').upper()
        cadastro_data_de_nascimento = input('Data de nascimento: ')
        cadastro_cpf = input('CPF: ')
        cpf_existente = False
        for verificacao in usuarios:
            if verificacao['CPF'] == cadastro_cpf:
                cpf_existente = True
                break
        if cpf_existente:
            print('Esse CPF já foi cadastrado. Verifique se você já tem uma conta ou se digitou corretamente.')
        else:
            numero_de_contas += 1
            adicionar_conta = '{:04}'.format(numero_de_contas)
            novo_usuario = {'nome': cadastro_nome, 'data de nascimento': cadastro_data_de_nascimento, 'CPF': cadastro_cpf, 'conta': adicionar_conta}
            usuarios.append(novo_usuario)
            print('Cadastro realizado com sucesso! Agora é só acessar com seu CPF e aproveitar nossos serviços.')
            print(usuarios)
    elif acessar == 'S':
        print('Obrigado por usar nossos serviços! Volte sempre!')
        break
    else:
        print('Opção inválida!')

    




        