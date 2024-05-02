lista = []


def adicionar(lista):

    if len(lista) >= 10:
        print('lista cheia')
    else:
        codigo= int(input('Informe o código do contato:'))
        cod_existe = any(contato['Código'] == codigo for contato in lista)
        if cod_existe:
            print('O código informado já pertence a um contato')
        else:
            nome = str(input('Digite o nome do contato:')).title()
            tel = int(input('Informe o telefone do contato: '))
            lista_add ={}
            lista_add['Código'] = codigo
            lista_add['Nome'] = nome
            lista_add['Telefone'] = tel
            lista.append(lista_add)
            print('CONTATO ADICIONADO COM SUCESSO!!')


def alterar():
    Nome = str(input('Digite o nome do contato que deseja editar:')).upper()
    for ctt in lista:
        if ctt['Nome'].upper() == Nome.upper():
            opc = int(input('Deseja alterar o nome?\n 1-sim\n 2-não\nR:'))
            if opc == 1:
                novo_nome =str(input('Digite o novo nome:'))
                ctt['Nome'] = novo_nome
            opc = int(input('Deseja alterar o telefone?\n 1-sim\n 2-não\nR:'))
            if opc == 1:
                tel = int(input('Digite o novo numero:'))
                ctt['Telefone'] = tel
            else:
                print(f'Este contato não existe')


def excluir():
    Nome = str(input('Digite o nome que deseja remover: ')).upper()
    for ctt in lista:
        if ctt['Nome'].upper() == Nome.upper():
            i =lista.index(ctt)
            lista.pop(i)
            break
        else:
            print('O contato não existe')


def listar_ctt():
    for contato in lista:
        for nome, telefone in contato.items():
            print(f'{nome}: {telefone}')


def list_cod():
    codi = int(input(f'Informe o código do seu contato:'))
    for contato in lista:
        for nome, telefone in contato.items():
            if contato == codi:
                print()
            print(f'{nome}, {telefone}')

def list_nome():
    Nome = str(input('Digite o nome do contato:')).upper()
    for ctt in lista:
        for nome, telefone in ctt.items():
            if ctt['Nome'].upper() == Nome.upper():
                print(f'{nome}: {telefone}')



def principal():


    while True:
        print('========================================================================')
        print('=                      MINHA AGENDA DE CONTATO                         =')
        print('========================================================================')
        print('=       1  -  Novo Contato                                             =')
        print('=       2  -  Alterar Contato                                          =')
        print('=       3  -  Excluir Contato                                          =')
        print('=       4  -  Listar Todos os Contatos                                 =')
        print('=       5  -  Listar Todos por Código do Contato                       =')
        print('=       6  -  Listar por Nome do Contato                               =')
        print('=       7  -  Sair                                                     =')
        print('========================================================================')
        opcao = int(input('Escolha a Opção :  '))

        if opcao == 1:
            adicionar(lista)
        elif opcao == 2:
            alterar()
        elif opcao == 3:
            excluir()
        elif opcao == 4:
            listar_ctt()
        elif opcao == 5:
            list_cod()
        elif opcao == 6:
            list_nome()
        elif opcao == 7:
            print('saindo...')
            break
        else:
            print(f'opção invalida.')


principal()
