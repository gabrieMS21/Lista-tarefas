from flask_cors import CORS

def init_app(app):
    CORS(app)
    app.config['JSON_SORT_KEYS'] = False
    app.config['SECRET_KEY'] = 'sua-chave-secreta-aqui'  # Em produção, use variáveis de ambiente 