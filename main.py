from aluno import Aluno
import os

def titulo(texto):
    return '*' * 30 + '\n' + texto.center(30) + '\n' + '*' * 30

def processar_opcao(opcao):
    aluno = Aluno
    print()
    if opcao == 1:
        print(titulo('Cadastrar aluno'))
        aluno.cadastra_aluno()

    elif opcao == 2:
        print(titulo('Listar alunos'))
        aluno.listar_alunos()
    elif opcao == 3:
        print('3')
    elif opcao == 4:
        print('4')
    elif opcao == 5:
        print('5')
    elif opcao == 6:
        print('6')
    elif opcao == 0:
        print('0')
    else:
        print('erro')
    

def menu():
    print(titulo('ACADEMIA FIT'))
    opcao = int(input("""
1 - Cadastrar aluno
2 - Listar alunos
3 - Buscar aluno
4 - Alterar aluno
5 - Remover aluno
6 - Alterar status
0 - Sair    
Escolha: """))
    processar_opcao(opcao)
    menu()
    

def main():
    os.system('cls')
    menu()

if __name__ == "__main__":
    main()