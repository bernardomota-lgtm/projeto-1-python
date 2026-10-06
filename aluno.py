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

    def __str__(self):
            return f'{self._id_aluno}'.ljust(15) + '|' + f'{self._nome}'.ljust(15) + '|' + f'{self._idade}'.ljust(15) + '|' + f'{self._telefone}'.ljust(15) + '|' + f'{self._email}'