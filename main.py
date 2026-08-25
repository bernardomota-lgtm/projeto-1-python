from aluno import Aluno
import os

def titulo(texto):
    os.system('cls')
    return '*' * 30 + '\n' + texto.center(30) + '\n' + '*' * 30

def processar_opcao(opcao):
    print()
    if opcao == '1':
        print(titulo('Cadastrar aluno'))
        Aluno.cadastrar_aluno()
    elif opcao == '2':
        print(titulo('Listar alunos'))
        Aluno.listar_alunos()
    elif opcao == '3':
        print(titulo('Buscando alunos'))
        nome = input('Digite o nome do aluno: ')
        Aluno.buscar_aluno(nome)
    elif opcao == '4':
        print(titulo('Alterar dados do aluno'))
        nome = input('Digite o nome do aluno: ')
        Aluno.buscar_aluno(nome)
        Aluno.alterar_aluno(nome)
    elif opcao == '5':
        print('5')
    elif opcao == '6':
        print('6')
    elif opcao == '0':
        print('Saindo')
        raise SystemExit
    else:
        print('erro')
    

def menu():
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
    processar_opcao(opcao)
    menu() # trocar a recurssao por while
    
def main():
    menu()

if __name__ == "__main__":
    main()