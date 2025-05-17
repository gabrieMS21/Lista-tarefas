class Tarefa:
    def __init__(self, id, titulo, concluida=False):
        self.id = id
        self.titulo = titulo
        self.concluida = concluida

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'concluida': self.concluida
        }

# Lista simulando banco de dados
tarefas = [
    Tarefa(1, 'Estudar Flask', False),
    Tarefa(2, 'Criar minha primeira API', False)
] 