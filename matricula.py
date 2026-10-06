from aluno import Aluno

class Matricula():
    lista_de_alunos = []

    @classmethod
    def cadastrar_aluno(cls):
        id_aluno = input('Id:')
        nome = input('Nome:')
        idade = input('Idade:')
        telefone = input('Telefone:')
        email = input('Email:')
        #plano = input()
        #status_matricula = input()
        cls.lista_de_alunos.append(Aluno(id_aluno, nome, idade, telefone, email))

    @classmethod
    def listar_alunos(cls):
        cls.cabecalho()
        for aluno in cls.lista_de_alunos:
            print(aluno)
        espera()

    @classmethod
    def buscar_aluno(cls, nome): # Fazer uma busca mais dinâmica. 
        cls.cabecalho()
        for aluno in cls.lista_de_alunos:
            if  nome == aluno._nome:
                print(aluno)
        espera()

    @classmethod
    def alterar_aluno(cls, nome):
        opcao = input("""
1 - Alterar nome
2 - Alterar idade
3 - Alterar telefone
4 - Alterar email
Escolha: """)
        if opcao == '1':
            novo_nome = input('Digite o novo nome: ')
            for aluno in cls.lista_de_alunos: # talvez reaproveitar o for da busca de alguma forma fatorar
                if nome == aluno._nome:
                    aluno._nome = novo_nome
        elif opcao == '2':
            nova_idade = input('Digite a nova idade: ')
            for aluno in cls.lista_de_alunos:
                if nome == aluno._nome:
                    aluno._idade = nova_idade
        elif opcao == '3':
            novo_telefone = input('Digite o novo número: ')
            for aluno in cls.lista_de_alunos:
                if nome == aluno._nome:
                    aluno._telefone = novo_telefone
        elif opcao == '4':
            novo_email = input('Digite o novo email: ')
            for aluno in cls.lista_de_alunos:
                if nome == aluno._nome:
                    aluno._email = novo_email
        espera()

    @classmethod

    def remover_aluno(cls, nome):
        cls.cabecalho
        decicao = input('Tem certeza que deseja apagar os dados do aluno: ' + nome + '\n' + 'digite [sim] ou [não]: ')
        if decicao == 'sim':
            for aluno in cls.lista_de_alunos:
                if nome == aluno._nome:
                    cls.lista_de_alunos.remove(aluno)
                    break
        espera()
        
    def cabecalho(): #print ou return?
        print('ID'.ljust(15) + '|' + 'NOME'.ljust(15) + '|' + 'IDADE'.ljust(15) + '|' + 'TELEFONE'.ljust(15) + '|' + 'EMAIL')
            
def espera():
    input('\nAperter enter para seguir')
