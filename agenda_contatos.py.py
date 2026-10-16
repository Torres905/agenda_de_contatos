agenda = []

def exibir_menu():
    print('\n' + '='*30)
    print('        AGENDA DE CONTATOS')
    print('='*30)
    print('1. Adicionar contato')
    print('2. Ver todos os contatos')
    print('3. Buscar contato')
    print('4. Editar contato')
    print('5. Excluir contato')
    print('6. Sair')
    print('='*30)

def adicionar_contato():
    nome = input('Nome: ').strip()
    telefone = input('Telefone: ').strip()
    email = input('E-mail: ').strip()

    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }

    agenda.append(contato)
    print(f'Contato "{nome}" adicionado com sucesso!')

def ver_todos():
    if len(agenda) == 0:
        print('A agenda está vazia.')
        return

    print('\n Seus Contatos:')
    print('-'*40)
    for indice, contato in enumerate(agenda):
        print(f'{indice+1}. Nome: {contato["nome"]}')
        print(f'Telefone: {contato["telefone"]}')
        print(f'E-mail: {contato["email"]}')
        print('-'*40)

def buscar_contato():
    termo = input('Digite o nome para buscar: ').strip().lower()
    encontrou = False

    for contato in agenda:
        if termo in contato["nome"].lower():
            print('\n Contato encontrado:')
            print(f'Nome: {contato["nome"]}')
            print(f'Telefone: {contato["telefone"]}')
            print(f'E-mail: {contato["email"]}')
            encontrou = True

    if not encontrou:
        print('Nenhum contato encontrado.')

def editar_contato():
    numero = int(input('Número do contato que deseja editar: ')) - 1

    if 0 <= numero < len(agenda):
        print(f'\nEditando: {agenda[numero]["nome"]}')
        novo_nome = input(f'Novo nome (deixe vazio para manter): ')
        novo_tel = input(f'Novo telefonr (deixe vazio para manter): ')
        novo_email = input(f'Novo email (deixe vazio para manter): ')

        if novo_nome:
            agenda[numero]["nome"] = novo_nome
        if novo_tel:
            agenda[numero]["telefone"] = novo_tel
        if novo_email:
            agenda[numero]["email"] = novo_email

        print('Contato atualizado!')
    else:
        print('Número inválido.')

def excluir_contato():
    numero = int(input('Número do contato que deseja excluir: ')) - 1

    if 0 <= numero < len(agenda):
        nome = agenda[numero]["nome"]
        agenda.pop(numero)
        print(f'Contato "{nome}" excluído!')
    else:
        print('Número inválido.')

while True:
    exibir_menu()
    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        ver_todos()
    elif opcao == '3':
        buscar_contato()
    elif opcao == '4':
        editar_contato()
    elif opcao == '5':
        excluir_contato()
    elif opcao == '6':
        print('Saindo da agenda... Até mais!')
        break
    else:
        print('Opção inválida. Tente de novo.')