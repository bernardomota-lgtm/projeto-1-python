from pessoa import Pessoa
import os

def menu():
    print('*' * 30)
    print('ACADEMIA FIT'.center(30))
    print('*' * 30)
    escolha = input("""
1 - Cadastrar aluno
2 - Listar alunos
3 - Buscar aluno
4 - Alterar aluno
5 - Remover aluno
6 - Alterar status
0 - Sair    
Escolha: """)
    print(escolha)

def main():
    os.system('cls')
    menu()

if __name__ == "__main__":
    main()