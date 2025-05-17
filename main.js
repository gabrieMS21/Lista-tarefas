const API_URL = 'http://localhost:5000/tarefas';
const lista = document.getElementById('lista-tarefas');
const form = document.getElementById('form-tarefa');
const input = document.getElementById('titulo');

// Carregar tarefas ao iniciar
window.onload = () => carregarTarefas();

// Função para carregar e mostrar tarefas
function carregarTarefas() {
    fetch(API_URL)
        .then(res => res.json())
        .then(tarefas => {
            lista.innerHTML = '';
            tarefas.forEach(tarefa => adicionarNaLista(tarefa));
        })
        .catch(err => console.error('Erro ao carregar tarefas:', err));
}

// Adiciona uma tarefa à lista visual
function adicionarNaLista(tarefa) {
    const li = document.createElement('li');
    li.innerHTML = `
        <span>${tarefa.titulo}</span>
        <button onclick="excluirTarefa(${tarefa.id})">🗑️</button>
    `;
    lista.appendChild(li);
}

// Lidar com envio do formulário
form.onsubmit = (e) => {
    e.preventDefault();
    const titulo = input.value.trim();

    if (titulo) {
        fetch(API_URL, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ titulo })
        })
        .then(res => res.json())
        .then(() => {
            input.value = '';
            carregarTarefas();
        })
        .catch(err => console.error('Erro ao adicionar tarefa:', err));
    }
};

// Excluir uma tarefa
function excluirTarefa(id) {
    fetch(`${API_URL}/${id}`, {
        method: 'DELETE'
    })
    .then(res => res.json())
    .then(() => carregarTarefas())
    .catch(err => console.error('Erro ao excluir tarefa:', err));
}
