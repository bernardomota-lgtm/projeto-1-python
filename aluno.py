
class Aluno():
    lista_de_alunos = []
    
    def __init__(self, id_aluno, nome, idade, telefone, email):
        self._id_aluno = id_aluno
        self._nome = nome
        self._idade = idade
        self._telefone = telefone
        self._email = email
        #self.plano = plano
        #self.data_matricula = data_matricula
        #self.status_matricula = status_matricula
        Aluno.lista_de_alunos.append(self)

    @staticmethod
    def cadastra_aluno():
        id_aluno = input('Id:')
        nome = input('Nome:')
        idade = input('Idade:')
        telefone = input('Telefone:')
        email = input('Email:')
        #plano = input()
        #status_matricula = input()
        Aluno(id_aluno, nome, idade, telefone, email)

    @classmethod
    def busca_aluno(cls, nome):
        Aluno.cabecalho()
        for aluno in cls.lista_de_alunos:
            if  nome == aluno._nome:
                print(aluno)
        espera()

    @classmethod
    def listar_alunos(cls):
        Aluno.cabecalho()
        for aluno in cls.lista_de_alunos:
            print(aluno)
        espera()
        
    def cabecalho(): #print ou return?
        print('ID'.ljust(15) + '|' + 'NOME'.ljust(15) + '|' + 'IDADE'.ljust(15) + '|' + 'TELEFONE'.ljust(15) + '|' + 'EMAIL')
            
    def __str__(self):
        return f'{self._id_aluno}'.ljust(15) + '|' f'{self._nome}'.ljust(15) + '|' f'{self._idade}'.ljust(15) + '|' f'{self._telefone}'.ljust(15) + '|' f'{self._email}'

def espera():
    input('\nAperter qualquer enter para seguir')
