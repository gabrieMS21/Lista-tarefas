from ..models.tarefa import Tarefa, tarefas

class TarefaController:
    @staticmethod
    def listar_tarefas():
        return [tarefa.to_dict() for tarefa in tarefas]

    @staticmethod
    def adicionar_tarefa(dados):
        if not dados or 'titulo' not in dados:
            return None, 'Campo "titulo" é obrigatório'

        nova_tarefa = Tarefa(
            id=len(tarefas) + 1,
            titulo=dados['titulo']
        )
        tarefas.append(nova_tarefa)
        return nova_tarefa.to_dict(), None

    @staticmethod
    def excluir_tarefa(id):
        global tarefas
        tarefas = [t for t in tarefas if t.id != id]
        return {'mensagem': 'Tarefa excluída com sucesso'} 