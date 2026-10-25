from matricula import Matricula

def menu_alterar_aluno(nome):
    opcao = input("""
1 - Alterar nome
2 - Alterar idade
3 - Alterar telefone
4 - Alterar email
Escolha: """)   
    alteracao = processar_opcao(opcao)
    Matricula.alterar_aluno(nome, opcao, alteracao)

def processar_opcao(opcao):
    if opcao == '1':
        alteracao = input('Digite o novo nome: ')
    elif opcao == '2':
        alteracao = input('Digite a nova idade: ')
    elif opcao == '3':
        alteracao = input('Digite o novo número: ')
    elif opcao == '4':
        alteracao = input('Digite o novo email: ')
    else:
        return -1
    return alteracao