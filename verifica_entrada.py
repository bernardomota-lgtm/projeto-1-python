def id_aluno(lista_de_alunos):
    if lista_de_alunos:
        id = lista_de_alunos[-1]._id_aluno + 1
        return id
    return 1