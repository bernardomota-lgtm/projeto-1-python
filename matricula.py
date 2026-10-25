from aluno import Aluno
import verifica_entrada

class Matricula():
    lista_de_alunos = []

    @classmethod
    def cadastrar_aluno(cls):
        id_aluno = verifica_entrada.id_aluno(cls.lista_de_alunos)
        nome = input('Nome:')
        idade = input('Idade:')
        telefone = input('Telefone:')
        email = input('Email:')
        #plano = input()
        status_matricula = input()
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
    def alterar_aluno(cls,nome, opcao, alteracao):
        if opcao == '1':
            for aluno in cls.lista_de_alunos: # talvez reaproveitar o for da busca de alguma forma fatorar
                if nome == aluno._nome:
                    aluno._nome = alteracao
        elif opcao == '2':
            for aluno in cls.lista_de_alunos:
                if nome == aluno._nome:
                    aluno._idade = alteracao
        elif opcao == '3':
            for aluno in cls.lista_de_alunos:
                if nome == aluno._nome:
                    aluno._telefone = alteracao
        elif opcao == '4':
            for aluno in cls.lista_de_alunos:
                if nome == aluno._nome:
                    aluno._email = alteracao
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
