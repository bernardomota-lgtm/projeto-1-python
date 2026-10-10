from matricula import Matricula
import os

def menu():
    condicao = False
    while not condicao: 
        print(titulo('ACADEMIA FIT'))
        opcao = input("""
    1 - Cadastrar aluno
    2 - Listar alunos
    3 - Buscar aluno
    4 - Alterar aluno
    5 - Remover aluno
    6 - Alterar status
    0 - Sair    
    Escolha: """)
        
        condicao = processar_opcao(opcao)

def processar_opcao(opcao):
    print()
    if opcao == '1':
        print(titulo('Cadastrar aluno'))
        Matricula.cadastrar_aluno()
    elif opcao == '2':
        print(titulo('Listar alunos'))
        Matricula.listar_alunos()
    elif opcao in '3 , 4, 5':
        print(titulo('Buscando alunos'))
        nome = input('Digite o nome do aluno: ')
        Matricula.buscar_aluno(nome)
        if opcao == '4':
            print(titulo('Alterar dados do aluno'))
            nome = input('Digite o nome do aluno: ')
            Matricula.alterar_aluno(nome)
        elif opcao == '5':
            print(titulo('Remover dados do aluno'))
            nome = input('Digite o nome do aluno: ')
            Matricula.remover_aluno(nome)
    elif opcao == '6':
        print('6')
    elif opcao == '0':
        print('Saindo')
        return True
    else:
        print('erro')

def titulo(texto):
    os.system('cls')
    return '*' * 30 + '\n' + texto.center(30) + '\n' + '*' * 30