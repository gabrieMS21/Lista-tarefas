from flask import Flask, send_from_directory
from .config.config import init_app
from .routes.tarefa_routes import tarefa_bp

def create_app():
    app = Flask(__name__, 
                static_folder='../frontend/static',
                template_folder='../frontend/templates')
    
    # Inicializa configurações
    init_app(app)
    
    # Registra blueprints
    app.register_blueprint(tarefa_bp)
    
    # Rotas para servir arquivos estáticos
    @app.route('/')
    def index():
        return send_from_directory('../frontend/templates', 'index.html')
    
    @app.route('/<path:filename>')
    def static_files(filename):
        return send_from_directory('../frontend/static', filename)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) 