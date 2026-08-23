
class Aluno():
    lista_de_alunos = []

    def __init__(self, id, nome, idade, telefone, email):
        self._id = id
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
        id = input('Id:')
        nome = input('Nome:')
        idade = input('Idade:')
        telefone = input('Telefone:')
        email = input('Email:')
        #plano = input()
        #status_matricula = input()
        Aluno(id, nome, idade, telefone, email)

    def __str__(self):
        return f'{self._id}'.ljust(15) + '|' f'{self._nome}'.ljust(15) + '|' f'{self._idade}'.ljust(15) + '|' f'{self._telefone}'.ljust(15) + '|' f'{self._email}'

    @classmethod
    def listar_alunos(cls):
        for aluno in cls.lista_de_alunos:
            print(aluno)
