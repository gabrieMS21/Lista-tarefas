from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Lista simulando banco de dados
tarefas = [
    {'id': 1, 'titulo': 'Estudar Flask', 'concluida': False},
    {'id': 2, 'titulo': 'Criar minha primeira API', 'concluida': False}
]

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('.', filename)

# Rota GET /tarefas
@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas), 200

# Rota POST /tarefas
@app.route('/tarefas', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.get_json()

    if not nova_tarefa or 'titulo' not in nova_tarefa:
        return jsonify({'erro': 'Campo "titulo" é obrigatório'}), 400

    nova_tarefa['id'] = len(tarefas) + 1
    nova_tarefa['concluida'] = False
    tarefas.append(nova_tarefa)

    return jsonify(nova_tarefa), 201

# Rota DELETE /tarefas/<id>
@app.route('/tarefas/<int:id>', methods=['DELETE'])
def excluir_tarefa(id):
    global tarefas
    tarefas = [t for t in tarefas if t['id'] != id]
    return jsonify({'mensagem': 'Tarefa excluída com sucesso'}), 200

# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True)
