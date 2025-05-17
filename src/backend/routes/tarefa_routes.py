from flask import Blueprint, request, jsonify
from ..controllers.tarefa_controller import TarefaController

tarefa_bp = Blueprint('tarefas', __name__)

@tarefa_bp.route('/tarefas', methods=['GET'])
def listar_tarefas():
    tarefas = TarefaController.listar_tarefas()
    return jsonify(tarefas), 200

@tarefa_bp.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    dados = request.get_json()
    tarefa, erro = TarefaController.adicionar_tarefa(dados)
    
    if erro:
        return jsonify({'erro': erro}), 400
    
    return jsonify(tarefa), 201

@tarefa_bp.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    resultado = TarefaController.excluir_tarefa(id)
    return jsonify(resultado), 200 